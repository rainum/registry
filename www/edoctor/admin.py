# django
from django.contrib import admin

# my
from edoctor.models import Doctor, Patient


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'second_name', 'specialization')


class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'second_name', 'doctor', 'date_of_receipt')


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
