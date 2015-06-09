from django.contrib import admin
from .models import Question, Reply, Patient
# Register your models here.

admin.site.register(Question)
admin.site.register(Reply)
admin.site.register(Patient)
