from django.db import models
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import UserManager 
from django.contrib.auth.models import AbstractUser


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "Cuidades"

    def __str__(self):
        return self.name

class ProService(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.name

class Host(AbstractUser):
    pass
    group=models.OneToOneField('auth.Group',unique=True, on_delete=False,null=True)


class PropertyUser(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    services= models.ManyToManyField(ProService)
    maxPax = models.IntegerField()
    image = models.ImageField(upload_to='img', null=True)
    dailyRate = models.IntegerField()
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)
    host = models.ForeignKey(Host, null=True, blank=True, on_delete=models.CASCADE) 

    class Meta:
        verbose_name_plural = "Propiedades"

    def __str__(self):
        return self.title

class Reservation(models.Model):
    total = models.IntegerField(blank=True, null=True)
    dateReservation = models.DateField(blank=False, null=False, auto_now=True)
    name = models.CharField(blank=True, null=True, max_length=50)
    lastname = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=200)
    propertyUser = models.ForeignKey(PropertyUser, on_delete=models.PROTECT, blank=False, null=False)
    
    class Meta:
        verbose_name_plural = "Reservas"

    def __str__(self):
        return self.name + ' ' + self.lastname + ' ' + self.propertyUser


class RentalDate(models.Model):
    starDate = models.DateField()
    endDate = models.DateField()
    propertyUser = models.ForeignKey(PropertyUser, null=True, blank=True, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Fechas de Reservas"

    def __str__(self):
        return  self.starDate.strftime('%d/%m/%Y') + " to " + self.endDate.strftime('%d/%m/%Y')

class RentalDateInline(admin.TabularInline):
    model = RentalDate
    fk_name = 'propertyUser'
    max_num = 7
class PropertyUserAdmin(admin.ModelAdmin):
    inlines = [RentalDateInline, ]
    

