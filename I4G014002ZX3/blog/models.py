from datetime import date, datetime
from time import timezone
from django.db import models
from django.contrib.auth.models import User

get_user_model = User

# Create your models here.


class Post (models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(None)
    Author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
