from urllib import request
from django import forms
from .models import users, Tip

class signupform(forms.Form):
	username = forms.CharField(label='username', required=True)
	password = forms.CharField(widget=forms.PasswordInput, label='password', required=True)
	cpassword = forms.CharField(widget=forms.PasswordInput, label='cpassword', required=True)

	def clean(self):
		cleaned_data = super().clean()
		if users.objects.filter(username=cleaned_data.get('username')).exists():
			raise forms.ValidationError("User already exists")
		password = cleaned_data.get("password")
		cpassword = cleaned_data.get("cpassword")
		print(str(password) + str(cpassword))
		if cpassword != password:
			raise forms.ValidationError("Passwords don't match")
		return cleaned_data

class signinform(forms.Form):
	username = forms.CharField(label='username',required=True)
	password = forms.CharField(widget=forms.PasswordInput, label='password', required=True)

	def clean(self):
		cleaned_data = super().clean()
		try:
			user = users.objects.get(username=cleaned_data.get('username'))
		except Exception as e:
			raise forms.ValidationError("User not registered")
		if user.password != cleaned_data.get('password'):
			raise forms.ValidationError("Password Doesn't Match")
		if user.dummy:
			raise forms.ValidationError("Trying to log in with dummy object")
		return cleaned_data

class TipForm(forms.ModelForm):
	class Meta:
		model = Tip
		fields = ['content',]