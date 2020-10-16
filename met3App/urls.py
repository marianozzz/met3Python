from django.urls import path

from met3App import views

urlpatterns = [

    path('', views.index, name="Inicio"),
]