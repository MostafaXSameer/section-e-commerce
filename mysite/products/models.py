from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from matplotlib import image
from sympy import false, true
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    desc = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50,unique=True)
    desc = models.TextField(max_length=5000)
    price = models.DecimalField(max_digits=10,default=0.0,decimal_places=2)
    image=models.ImageField(upload_to='photos/%y/%m/%d',default='none')
    active=models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='product',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Review(models.Model):
    message = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product,related_name='review',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='review',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

