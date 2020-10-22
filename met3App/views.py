from django.shortcuts import render, HttpResponse
from django.template import Template,Context
from django.template import loader
from met3App.models import *

# Create your views here.

class Propiedad(object):
    def __init__(self,title):
        self.title=title

def index(request):

    p1=Propiedad("propiedad 1")
    p2=Propiedad("propiedad 2")
    propiedades=[p1,p2]
    cuidades=["mar del plata","Necochea"]

    #doc_externo=loader.get_template('home.html')
    #doc=doc_externo.render({"propiedades":propiedades,"cuidades":cuidades})
    return render(request,'home.html',{"propiedades":propiedades,"cuidades":cuidades})
    #return render(request, "met3App/home.html")

    
def prueba(request){

    varia=City.objects.filter(name='Mar del Plata')
} 