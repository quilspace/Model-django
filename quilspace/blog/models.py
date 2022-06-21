from django.conf import settings
from django.db import models


# Create your models here.
class Post(models.Model):
    Tile = models.CharField(max_length=200)
    Text = models.CharField(max_length=1000)
    Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    Publised_date = models.DateTimeField(auto_now_add=True)
