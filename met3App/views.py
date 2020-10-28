from django.shortcuts import render, HttpResponse
from django.template import Template,Context
from django.template import loader
from met3App.models import *

# Create your views here.

def home(request):
    
    Properties=PropertyUser.objects.all()
    return render(request, "met3App/home.html",{"Properties":Properties})

def login(request):
    return  render(request, "met3App/login.html")

def details(request,id):
    idpropiedad = PropertyUser.objects.get(id=id)
    return  render(request, "met3App/details.html",{"idpropiedad":idpropiedad})

def about_us(request):
    return  render(request, "met3App/about_us.html")

