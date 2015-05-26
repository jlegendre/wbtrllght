from django.db import models
from django.utils import timezone

# Create your models here.

class Center(models.Model):
    center_number = models.CharField(max_length=50)
    center_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.center_name

class Patient(models.Model):
    center = models.ForeignKey(Center, default=1)
    initials = models.CharField(max_length=50)
    status = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date published')
    modification_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.initials + ' - ' + self.status

class Ecrf(models.Model):
    ecrf_name = models.CharField(max_length=50)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date')
    theoritical_number_of_patients = models.CharField(max_length=50)

    def __unicode__(self):
        return self.ecrf_name







