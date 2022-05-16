from django.urls import path
from . import views

urlpatterns=[
    path('product/<str:id>',views.product,name='product'),

    path('',views.products,name='products'),
    
    path('electronics',views.electronics,name='electronics'),
    
    path('electronics/product/<str:id>',views.product,name='elctroproduct'),
    
    path('clothes',views.clothes,name='clothes'), 
    
    path('clothes/product/<str:id>',views.product,name='cloproduct'),
    
    path('watches',views.watches,name='watches'),
    
    path('watches/product/<str:id>',views.product,name='watchproduct'),
    
    path('sports',views.sports,name='sports'),
    
    path('sports/product/<str:id>',views.product,name='spoproduct'),

]