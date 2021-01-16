# NEWS/models.py

from __future__ import unicode_literals
from django.db import models


# Create your models here.
class News(models.Model):

	title 	= models.CharField(max_length=50)
	summary	= models.TextField()
	body   	= models.TextField()
	date 	= models.CharField(max_length=12)
	image 	= models.TextField()
	author 	= models.CharField(max_length=50)

	def __str__(self):
		return self.name