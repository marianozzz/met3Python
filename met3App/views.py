from django.shortcuts import render, HttpResponse
from django.template import Template,Context
from django.template import loader
from met3App.models import *

# Create your views here.

def home(request):
    
    Properties=PropertyUser.objects.all()
    #Properties=PropertyUser.objects.filter(propertyuser__propertyuser_services)
    #prueba para traer de la db
    for pro in Properties:
        print(pro.title)
        print(pro.description)  
        print(pro.services)
        print(pro.maxPax)
        print(pro.image)
        print(pro.dailyRate)
        print(pro.city)
        print(pro.host)
        
    #--------------------------------
    
    return render(request, "met3App/home.html",{"Properties":Properties})

def login(request):
    return  render(request, "met3App/login.html")

def details(request, id):
    idpropiedad = PropertyUser.objects.get(id=id)
    #prop = PropertyUser.objects.filter(id)
    #return  render(request, "met3App/details.html",{"prop":prop})
    return  render(request, "met3App/details.html",{"idpropiedad":idpropiedad})

def about_us(request):
    return  render(request, "met3App/about_us.html")



