from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):

    return render(request, "met3App/home.html")

def login(request):
    return  render(request, "met3App/login.html")