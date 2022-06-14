from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

class LoginForm(forms.Form):
	username = forms.CharField(label='username',required=True)
	password = forms.CharField(widget=forms.PasswordInput, label='password', required=True)

	def clean(self):
		cleaned_data = super().clean()
		try:
			user = User.objects.get(username=cleaned_data.get('username'))
		except Exception as e:
			raise forms.ValidationError("User not registered")
		if not user.check_password(cleaned_data.get('password')):
			raise forms.ValidationError("Password Doesn't Match")
		return cleaned_data

class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

class PublishForm(forms.ModelForm):
	class Meta:
		model = models.Article
		fields = ['title', 'synopsis', 'content']

class FavoriteForm(forms.ModelForm):
	class Meta:
		model = models.UserFavouriteArticle
		fields = []