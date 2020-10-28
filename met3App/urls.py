from django.urls import path
from met3App import views
from django.conf import settings


urlpatterns = [

    path('', views.home, name="Home"),
    path('login/', views.login, name="Login"),
    path('details/<int:id>/', views.details, name="Details"),
    path('about-us/', views.about_us, name="About"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)