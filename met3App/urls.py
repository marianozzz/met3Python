from django.urls import path
from met3App import views
from django.conf import settings


urlpatterns = [

    path('', views.home, name="Home"),
    path('login/', views.login, name="Login"),
    path('details/', views.details, name="Details"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)