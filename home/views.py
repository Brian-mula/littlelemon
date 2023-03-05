from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    context= Menu.objects.all()
    return render(request, 'menu.html', context={'menues':context})

def book(request):
    return render(request,'book.html')