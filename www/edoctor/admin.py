# django
from django.contrib import admin

# my
from edoctor.models import Doctor, Talon, Address


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'second_name', 'specialization')


class TalonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'second_name', 'doctor', 'address', 'date_of_receipt')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'street', 'house')


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Talon, TalonAdmin)
admin.site.register(Address, AddressAdmin)
