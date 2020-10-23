from django.contrib import admin
from met3App.models import City, PropertyUser , Reservation, RentalDate
# Register your models herePropertyUser.

admin.site.register(City)
admin.site.register(PropertyUser)
admin.site.register(Reservation)
admin.site.register(RentalDate)