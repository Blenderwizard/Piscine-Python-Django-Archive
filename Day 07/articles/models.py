from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=64, blank=False)
	author = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, blank=False)
	synopsis = models.CharField(max_length=312, blank=False)
	content = models.TextField(blank=False)
	id = models.IntegerField(primary_key=True)

	def __str__(self):
		return str(self.title)

class UserFavouriteArticle(models.Model):
	user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
	article = models.ForeignKey(Article, blank=False, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.article)
	