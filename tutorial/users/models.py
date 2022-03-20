from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20 , blank=False , default='' )
    password = models.CharField(max_length= 100  ,default= '')
    email = models.CharField(max_length=100, default='')