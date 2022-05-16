from re import X
from django.shortcuts import render

 
def index (request):
    data={'name':'Mostafa','age':'22'}
    return render(request,'pages/index.html',data)

def about (request):
    data={'name':'Mostafa','age':'23'}
    return render(request,'pages/about.html',data)

