from django.shortcuts import render
from .models import Product
from .models import Category
from .models import Review
# Create your views here.

def products(request):
    return render(request,'products/products.html',{
        'pro':Product.objects.order_by('-id'),
        'cat':Category.objects.all(),
        'rev':Review.objects.all() })

def product(request,id):
    return render(request,'products/product.html',{
        'pro':Product.objects.get(id=id),
        'cat':Category.objects.all(),})

def elctroproduct(request,id):
    return render(request,'products/product.html',{
        'pro':Product.objects.get(id=id),
        'cat':Category.objects.all(),})

def cloproduct(request,id):
    return render(request,'products/product.html',{
        'pro':Product.objects.get(id=id),
        'cat':Category.objects.all(),})    

def watchproduct(request,id):
    return render(request,'products/product.html',{
        'pro':Product.objects.get(id=id),
        'cat':Category.objects.all(),})    

def spoproduct(request,id):
    return render(request,'products/product.html',{
        'pro':Product.objects.get(id=id),
        'cat':Category.objects.all(),})


def electronics(request):
    return render(request,'products/electronics.html',{
        'ele':Product.objects.filter(cat_id=1),
        'cat':Category.objects.all(),})

def clothes(request):
    return render(request,'products/clothes.html',{
        'col':Product.objects.filter(cat_id=2),
        'cat':Category.objects.all(),})

def watches(request):
    return render(request,'products/watches.html',{
        'wat':Product.objects.filter(cat_id=4),
        'cat':Category.objects.all(),})

def sports(request):
    return render(request,'products/sports.html',{
        'spo':Product.objects.filter(cat_id=5),
        'cat':Category.objects.all(),})