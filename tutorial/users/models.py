from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255, default=None)
    username = None
    password = models.CharField(max_length= 255)
    email = models.CharField(max_length=100, default='' , unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []