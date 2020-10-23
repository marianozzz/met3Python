from django.urls import path

from met3App import views

urlpatterns = [

    path('', views.home, name="Home"),
    path('login/', views.login, name="Login"),
]