from django.db import models

# Create your models here.

class User(models.Model):

    name:str=models.TextField(max_length=30)
    password:str=models.TextField(max_length=30)


class Student(models.Model):
    name=models.TextField(max_length=35,null=False)
    cclass=models.TextField(max_length=3,null=False)
    fee=models.IntegerField(default=18000,null=True)
    gender=models.TextField(null=False)


