from django.shortcuts import render, HttpResponse
from django.template import Template,Context
from django.template import loader
from met3App.models import *

# Create your views here.

def home(request):
    
    Properties=PropertyUser.objects.all()
    #Properties=PropertyUser.objects.filter(propertyuser__propertyuser_services)
    #--prueba para traer de la db
  # for pro in Properties:
   #     print(pro.title) 
   #    print(pro.dailyRate)
   #    print(pro.services)
    #--------------------------------
    
    return render(request, "met3App/home.html",{"Properties":Properties})

def login(request):
    return  render(request, "met3App/login.html")

def details(request):
    return  render(request, "met3App/details.html")



