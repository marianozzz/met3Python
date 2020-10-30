from django.urls import path
from met3App import views
from django.conf import settings
from met3App.views import Login, log_out

urlpatterns = [

    path('', views.home, name="Home"),
    path('login/', Login.as_view() , name='Login'),
    path('logout/',log_out, name='logout'),
    path('details/<int:id>/', views.details, name="Details"),
    path('search/', views.search, name="Search"),
    path('about-us/', views.about_us, name="About"),
    path('reserva/<int:id>/', views.reserva, name="reserva"),
    path('myproperty/', views.my_property, name="myproperty"),
    path('myreservation/<int:id>/', views.my_reservation, name="myreservation"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)