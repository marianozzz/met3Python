from django.shortcuts import render, HttpResponse
from django.template import Template,Context
from django.template import loader
from met3App.models import *
from datetime import date

# Create your views here.

def home(request):
    
    ProAll=PropertyUser.objects.all()
    return render(request, "met3App/home.html",{"Properties":ProAll})

def login(request):
    return  render(request, "met3App/login.html")

def details(request,id):
    propertyUser= PropertyUser.objects.get(id=id)
    rentalsDate = RentalDate.objects.filter(propertyUser=propertyUser,reservation__isnull=True)
    rentalsDate= list(rentalsDate)
    context={"propertyUser":propertyUser, "rentalsDate": rentalsDate}

    return  render(request, "met3App/details.html",context)


def about_us(request):
    return  render(request, "met3App/about_us.html")

