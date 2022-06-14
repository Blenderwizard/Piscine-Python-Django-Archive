import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from . import forms
from . import models

def index(request):
	if request.user.is_authenticated:
		if request.user.is_superuser and not models.users.objects.filter(username = request.user, dummy=True).exists():
			user = models.users(username = request.user, password = request.user, dummy=True)
			user.save()
		request.COOKIES['username'] = request.user
		if request.method == 'POST':
			if 'delete' in request.POST and 'id' in request.POST:
				if models.Tip.objects.filter(id=int(request.POST['id'])).exists():
					tip = models.Tip.objects.get(id=int(request.POST['id']))
					if request.user.is_superuser:
						tip.delete()
					elif tip.author == models.users.objects.get(username=request.user):
						tip.delete()
				form = forms.TipForm()
			elif 'upvote' in request.POST and 'id' in request.POST:
				if models.Tip.objects.filter(id=int(request.POST['id'])).exists():
					tip = models.Tip.objects.get(id=int(request.POST['id']))
					if not tip.upvoted.filter(username=request.user).exists():
						tip.upvoted.add(models.users.objects.get(username=request.user))
						if tip.downvoted.filter(username=request.user).exists():
							tip.downvoted.remove(models.users.objects.get(username=request.user))
						tip.save()
					else:
						tip.upvoted.remove(models.users.objects.get(username=request.user))
						tip.save()
				form = forms.TipForm()
			elif 'downvote' in request.POST and 'id' in request.POST:
				if models.Tip.objects.filter(id=int(request.POST['id'])).exists():
					tip = models.Tip.objects.get(id=int(request.POST['id']))
					if not tip.downvoted.filter(username=request.user).exists():
						if request.user.is_superuser:
							dummy = models.users.objects.get(username=request.user, dummy=True)
							tip.downvoted.add(dummy)
							if tip.upvoted.filter(username=request.user).exists():
								tip.upvoted.remove(dummy)
							tip.save()
						elif tip.author == models.users.objects.get(username=request.user):
							tip.downvoted.add(models.users.objects.get(username=request.user))
							if tip.upvoted.filter(username=request.user).exists():
								tip.upvoted.remove(models.users.objects.get(username=request.user))
							tip.save()
					else:
						tip.downvoted.remove(models.users.objects.get(username=request.user))
						tip.save()
				form = forms.TipForm()
			else:
				form = forms.TipForm(request.POST)
				if form.is_valid():
					user = models.users.objects.get(username=request.user)
					newTip = models.Tip(author=user,content=form.cleaned_data.get('content'))
					newTip.save()
		else :
			form = forms.TipForm()
		response = render(request, 'index.html', {
			"request" : request,
			'login' : True,
			'form' : form,
			'tips': models.Tip.objects.all()
		})
		response.set_cookie('username', request.user, 1000000000)
		return response
	elif 'username' not in request.COOKIES:
		username = random.choice(settings.NAMES)
		request.COOKIES['username'] = username
		response = render(request, 'index.html', {
			"request" : request,
			'login' : False,
			'tips': models.Tip.objects.all()
		})
		response.set_cookie('username', username, 42)
		return response
	
	return render(request, 'index.html', {
		'login' : False,
		'tips': models.Tip.objects.all()
	})

def signup(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		form = forms.signupform(request.POST)
		if form.is_valid():
			m = models.users(username = form.cleaned_data.get('username'), password = form.cleaned_data.get('password'), dummy=False)
			user = User.objects.create(username = form.cleaned_data.get('username'), password = form.cleaned_data.get('password'))
			user.save()
			m.save()
			login(request, user)
			return redirect('/')
	elif 'username' not in request.COOKIES:
		username = random.choice(settings.NAMES)
		request.COOKIES['username'] = username
		form = forms.signupform()
		response = render(request, 'signup.html', {
			'form' : form
		})
		response.set_cookie('username', username, 42)
		return response
	else :
		form = forms.signupform()
	return render(request, 'signup.html', {
		'form' : form
	})

def signin(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		form = forms.signinform(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = User.objects.get(username=username,password=password)
			login(request, user)
			return redirect('/')
	elif 'username' not in request.COOKIES:
		username = random.choice(settings.NAMES)
		request.COOKIES['username'] = username
		form = forms.signupform()
		response = render(request, 'signup.html', {
			'form' : form
		})
		response.set_cookie('username', username, 42)
		return response
	else :
		form = forms.signinform()
	return render(request, 'signin.html', {
		'form' : form
	})

def logout_view(request):
	if request.user.is_authenticated:
		logout(request)
	response = redirect('/')
	response.delete_cookie('username')
	return response