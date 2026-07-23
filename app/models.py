from django.db import models

# Create your models here.

class User(models.Model):

    name:str=models.TextField(max_length=30)
    password:str=models.TextField(max_length=30)
    