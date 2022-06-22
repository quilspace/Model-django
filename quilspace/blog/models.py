from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Post(models.Model):
    Tile = models.CharField(max_length=200)
    Text = models.CharField(max_length=1000)
    Author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    Created_date = models.DateTimeField(auto_now_add=True)
    Publised_date = models.DateTimeField(auto_now_add=True)
