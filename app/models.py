from os import name
from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=150)

class Sub_Category(models.Model):
     name=models.CharField(max_length=150)
     category = models.ForeignKey(Category,on_delete=models.CASCADE)