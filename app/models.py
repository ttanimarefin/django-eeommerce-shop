from os import name
from django.db import models
import sys

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Sub_Category(models.Model):
     name = models.CharField(max_length=264)
     category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    
     def __str__(self):
        return self.name
    


class Product(models.Model):
    category= models.ForeignKey(Category,on_delete=models.CASCADE, null=False,default='')
    Sub_category=models.ForeignKey(Sub_Category,on_delete=models.CASCADE, null=False, default='')
    image= models.ImageField(upload_to='ecommerce/pimg')
    name=models.CharField(max_length=100)
    price=models.IntegerField
    date=models.DateField(auto_now_add=True)
