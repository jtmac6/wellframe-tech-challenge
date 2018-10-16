from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Patient, Medication, Prescription

admin.site.register(Patient)
admin.site.register(Medication)
admin.site.register(Prescription)
