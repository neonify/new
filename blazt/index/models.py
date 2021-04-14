from django.db import models

# Create your models here.

class songs(models.Model):
  name = models.CharField(max_length=30)
  desc = models.CharField(max_length=50)
  spic = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
 
 
