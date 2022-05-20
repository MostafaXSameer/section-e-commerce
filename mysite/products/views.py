from django.shortcuts import render
from .models import Product
from .models import Category
from .models import Review
from cart.forms import CartAddProductForm
# Create your views here.

def products(request):
    return render(request,'products/products.html',{
        'pro':Product.objects.order_by('id'),
        'cat':Category.objects.all(),
        'rev':Review.objects.all() 
        })

def product(request,id):
    cart_product_form = CartAddProductForm()
    return render(request,'products/product.html',{
        'pro':Product.objects.get(id=id),
        'cat':Category.objects.all(),
        'cart_product_form':CartAddProductForm
        })

def category(request,id):
    return render(request,'products/category.html',{
        'pro':Product.objects.all().filter(cat=id),
        'cat':Category.objects.all()
    })

def cart(request):
    return render(request,'products/cart.html',{
        'cat':Category.objects.all(),
        
        })