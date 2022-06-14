from datetime import datetime
from django.views.generic import RedirectView, ListView, FormView, DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse
from . import models
from . import forms

class home(RedirectView):
	pass

class articles(ListView):
	model = models.Article
	template_name = "articles.html"

	def get_context_data(self, **kwargs):
		context = super(articles, self).get_context_data(**kwargs)
		context['object_list'] = models.Article.objects.order_by('-created')
		context['isuser'] = self.request.user.is_authenticated
		if self.request.user.is_authenticated:
			context['username'] = self.request.user
		return context

class loginView(FormView):
	model = User
	form_class = forms.LoginForm
	template_name = "login.html"
	success_url = '/'

	fields = ['username', 'password']

	def form_valid(self, form):
		if self.request.user.is_authenticated:
			return HttpResponse("You are already authenticated as " + str(self.request.user))
		user = User.objects.get(username=form.cleaned_data.get('username'))
		login(self.request, user)
		return HttpResponseRedirect(self.get_success_url())

	def get_context_data(self, **kwargs):
		context = super(loginView, self).get_context_data(**kwargs)
		context['isuser'] = self.request.user.is_authenticated
		if self.request.user.is_authenticated:
			context['username'] = self.request.user
		return context

class logoutView(RedirectView):
	url='/'

	def get_redirect_url(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			logout(self.request)
		return super(logoutView, self).get_redirect_url(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(logoutView, self).get_context_data(**kwargs)
		context['isuser'] = self.request.user.is_authenticated
		if self.request.user.is_authenticated:
			context['username'] = self.request.user
		return context

class RegisterView(CreateView):
	model = User
	form_class = forms.RegisterForm
	template_name = "register.html"
	success_url = "/"

	def form_valid(self, form):
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(RegisterView, self).get_context_data(**kwargs)
		context['isuser'] = self.request.user.is_authenticated
		if self.request.user.is_authenticated:
			context['username'] = self.request.user
		return context


class Publications(ListView):
	model = models.Article
	template_name = "publications.html"

	def get_context_data(self, **kwargs):
		context = super(Publications, self).get_context_data(**kwargs)
		context['isuser'] = self.request.user.is_authenticated
		if self.request.user.is_authenticated:
			context['username'] = self.request.user
		if not self.request.user.is_authenticated:
			return context
		context['object_list'] = list(models.Article.objects.filter(author=self.request.user))
		return context

class Detail(CreateView):
	model = models.UserFavouriteArticle
	form_class = forms.FavoriteForm
	template_name = "detail.html"
	success_url = "/"

	def get_context_data(self, **kwargs):
		context = super(Detail, self).get_context_data(**kwargs)
		context['isuser'] = self.request.user.is_authenticated
		if self.request.user.is_authenticated:
			context['username'] = self.request.user
		context['article'] = models.Article.objects.get(id=int(self.kwargs['pk']))
		return context

	def form_valid(self, form):
		print(self.kwargs['pk'])
		form.instance.user = self.request.user
		form.instance.article = models.Article.objects.get(id=int(self.kwargs['pk']))
		return super(Detail, self).form_valid(form)
	
class Favourites(ListView):
	model = models.UserFavouriteArticle
	template_name = "favourites.html"

	def get_context_data(self, **kwargs):
		context = super(Favourites, self).get_context_data(**kwargs)
		context['isuser'] = self.request.user.is_authenticated
		if self.request.user.is_authenticated:
			context['username'] = self.request.user
		if not self.request.user.is_authenticated:
			return context
		context['object_list'] = models.UserFavouriteArticle.objects.filter(user=self.request.user)
		print(context['object_list'])
		return context

class Publish(CreateView):
	model = models.Article
	form_class = forms.PublishForm
	template_name = "publish.html"
	success_url = "/articles"

	def form_valid(self, form):
		user = self.request.user
		form.instance.author = user
		return super(Publish, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(Publish, self).get_context_data(**kwargs)
		context['isuser'] = self.request.user.is_authenticated
		if self.request.user.is_authenticated:
			context['username'] = self.request.user
		return context
