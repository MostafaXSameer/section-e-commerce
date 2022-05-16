from django.contrib import admin
from numpy import product
from .models import Category, Product, Review
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
