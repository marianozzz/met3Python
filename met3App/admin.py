from django.contrib import admin
from met3App.models import City, PropertyUser ,PropertyUserAdmin, Reservation, RentalDate, ProService, Host
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

# Register your models herePropertyUser.
class GroupInline(admin.StackedInline):
    model=Host
    can_delete = False
    verbose_name_plural = 'Grupo Host'

class GroupAdmin(BaseGroupAdmin):
    inlines = (GroupInline, )


admin.site.register(City)
admin.site.register(PropertyUser,PropertyUserAdmin)
admin.site.register(Reservation)
#admin.site.register(RentalDate)
admin.site.register(ProService)
admin.site.register(Host,UserAdmin)
# Re-register GroupAdmin
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
