from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = get_user_model()
    Created_date = models.DateTimeField(blank=True)
    Published_date = models.DateTimeField(blank=True)
