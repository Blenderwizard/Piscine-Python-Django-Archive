from django.contrib import admin
from .models import Article, UserFavouriteArticle
from django.contrib.auth.models import User

class ArticleAdmin(admin.ModelAdmin):
	model = Article
	fields = ['title','author','synopsis','content']

class UserFavouriteArticleAdmin(admin.ModelAdmin):
	model = UserFavouriteArticle
	fields = ['user', 'article']

admin.site.register(Article, ArticleAdmin)
admin.site.register(UserFavouriteArticle, UserFavouriteArticleAdmin)
