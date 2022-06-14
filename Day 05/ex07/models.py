from django.db import models

# Create your models here.

class Movies(models.Model):
	title = models.CharField(max_length = 64, blank=False, unique=True)
	episode_nb = models.IntegerField(primary_key=True, blank=False)
	opening_crawl = models.TextField(blank=True)
	director = models.CharField(max_length = 32, blank=False)
	producer = models.CharField(max_length = 128, blank=False)
	release_date = models.DateField(blank=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
 