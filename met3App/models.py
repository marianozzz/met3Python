from django.db import models
#from django.contrib.auth.models import Host

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name

class PropertyUser(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    services= models.CharField(max_length=500)
    maxPax = models.IntegerField()
    #image = models.ImageField(upload_to='images', max_length=100)
    dailyRate = models.IntegerField()
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)
    #host = models.ForeignKey(Host, null=False, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = "PropertiesUser"

    def __str__(self):
        return self.title


class Reservation(models.Model):
    total = models.IntegerField(blank=True, null=True)
    dateReservation = models.DateField(blank=False, null=False, auto_now=True)
    name = models.CharField(blank=True, null=True, max_length=50)
    lastname = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=200)
    propertyUser = models.ForeignKey(PropertyUser, on_delete=models.PROTECT, blank=False, null=False)
    
    def __str__(self):
        return self.name + ' ' + self.lastname + ' ' + self.propertyUser


class RentalDate(models.Model):
    starDate = models.DateField()
    endDate = models.DateField()
    propertyUser = models.ForeignKey(PropertyUser, null=True, blank=True, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name_plural = "RentalDates"

    def __str__(self):
        return  self.starDate 
