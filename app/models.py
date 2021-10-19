from os import name
from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Sub_Category(models.Model):
     name=models.CharField(max_length=150)
     category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    


class Product(models.Model):
    image= models.ImageField(upload_to='ecommerce/pimg')
    name=models.CharField(max_length=100)
    price=models.IntegerField
    date=models.DateField(auto_now_add=True)
