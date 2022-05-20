from django.urls import path
from . import views

urlpatterns=[
    path('product/<str:id>',views.product,name='product'),


    path('',views.products,name='products'),


    path('category/<str:id>',views.category,name='category'),

]