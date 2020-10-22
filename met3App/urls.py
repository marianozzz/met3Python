from django.urls import path

from met3App import views
from met3App.views import index
urlpatterns = [

    path('', views.index, name="Inicio"),
    path('home/',index),

]