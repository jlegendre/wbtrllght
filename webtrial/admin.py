from django.contrib import admin
from .models import Patient, Center, Ecrf

# Register your models here.

admin.site.register(Patient)
admin.site.register(Center)
admin.site.register(Ecrf)



