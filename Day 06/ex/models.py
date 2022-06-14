from django.db import models

# Create your models here.

class users(models.Model):
	username = models.TextField(blank=False, unique=True)
	password = models.TextField(blank=False)
	dummy = models.BooleanField(blank=True)
	id = models.IntegerField(primary_key=True, blank=False)

	def __str__(self):
		return self.username
 
class Tip(models.Model):
	content = models.TextField(blank=False)
	author = models.ForeignKey(users, blank=False, on_delete=models.CASCADE, related_name='author')
	date = models.DateTimeField(blank=False, auto_now_add=True)
	upvoted = models.ManyToManyField(users, blank=True, related_name='upvotes')
	downvoted = models.ManyToManyField(users, blank=True, related_name='downvotes')
	id = models.IntegerField(blank=False, primary_key=True)