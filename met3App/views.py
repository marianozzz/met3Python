from django.db.models.query_utils import Q
from django.shortcuts import render, HttpResponse
from django.template import Template,Context
from django.template import loader
from django.db.models import Q
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
    context={"propertyUser":propertyUser, "rentalsDate": rentalsDate, "loop_maxpax": range(1, propertyUser.maxPax+1)}

    return  render(request, "met3App/details.html",context)

def search(request):
    ProAll=City.objects.all()
    return  render(request, "met3App/search.html",{"ProAll":ProAll})
    
def result (request): 
    queryset_city = request.GET.get("ciudad")
    queryset_pax = request.GET.get("huespedes")
    start_date = request.GET.get("desde")
    end_date = request.GET.get("hasta")
   
    
    #print(queryset_city)
    resultado=PropertyUser.objects.all()
    
    if queryset_city:
        resultado = PropertyUser.objects.filter(
                    Q(city_id = queryset_city) &
                    Q(maxPax = queryset_pax)
                    ).distinct()
    return render(request, "met3App/result.html",{"resultado": resultado})

def about_us(request):
    
    return  render(request, "met3App/about_us.html")


def reserva(request,id):
    if request.method == 'POST':
        
        pro = PropertyUser.objects.get(id=request.POST['propertyId'])
        na=request.POST['name']
        lastn=request.POST['lastname']
        ema=request.POST['email']
        to= (abs((datetime.strptime(request.POST['dateTo'], '%m/%d/%Y')) - (datetime.strptime(request.POST['dateFrom'], '%m/%d/%Y'))).days) * pro.dailyRate
        
        r = Reservation(
            startDate=datetime.strptime(request.POST['dateFrom'], '%m/%d/%Y').date(),
            endDate=datetime.strptime(request.POST['dateTo'], '%m/%d/%Y').date(),
            name=na,
            lastname=lastn,
            email=ema,
            propertyUser=PropertyUser.objects.get(id=request.POST['propertyId']),
            total=to
        )
        r.save()
         
    return  render(request, "met3App/home.html")
