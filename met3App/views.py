from django.shortcuts import render, HttpResponse, redirect
from django.template import Template,Context
from django.template import loader
from met3App.models import *
from datetime import date
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from .forms import FormLogin
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.

def home(request):
    ProAll=PropertyUser.objects.all()
    return render(request, "met3App/home.html",{"Properties":ProAll})


def my_property(request):
    current_user = request.user
    ProAll=PropertyUser.objects.filter(host= current_user)
    return render(request, "met3App/myproperty.html",{"Properties":ProAll})


def my_reservation(request, id):

    propertyUser=PropertyUser.objects.get(id=id)
    reservation = list(Reservation.objects.filter(propertyUser=propertyUser))
    context={"propertyUser":propertyUser, "reservation":reservation}
    return render(request, "met3App/myreservation.html", context)

def details(request,id):
    propertyUser= PropertyUser.objects.get(id=id)

    reservation= Reservation.objects.filter(propertyUser=propertyUser)
    rentalsDate= RentalDate.objects.filter(propertyUser=propertyUser)
    rentalsDate= list(rentalsDate)
    
    if reservation:       
      for r in reservation:
        for rd in rentalsDate:
            if r.startDate == rd.startDate and r.endDate == rd.endDate:
                rd.delete()
                rentalsDate.remove(rd)
            elif r.startDate == rd.startDate:
                 rd.startDate = r.endDate
            elif r.startDate > rd.startDate and r.endDate <= rd.endDate:
                    aux2=rd.endDate
                    rd.endDate=r.startDate

                    aux= RentalDate(
                        startDate= r.endDate,
                        endDate= aux2,
                        propertyUser= propertyUser)
                    aux.save()
                    rentalsDate.append(aux)
    


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
         
    return  render(request, "met3App/success.html")




class Login(FormView):
    template_name= 'met3App/login.html'
    form_class= FormLogin
    success_url= reverse_lazy('myproperty')

    @method_decorator(csrf_protect) #decoradores de seguridad/proteccion
    @method_decorator(never_cache)
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login,self).form_valid(form)



def log_out(request):
    logout(request)
    return redirect('Home')
