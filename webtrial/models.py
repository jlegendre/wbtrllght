from django.db import models

# Create your models here.

class Patient(models.Model):
    initials = models.CharField(max_length=50)
    status = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date published')
    modification_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return str(self.initials) + ' - ' + str(self.status)

class Center(models.Model):
    center_number = models.CharField(max_length=50)
    center_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    def __unicode__(self):
        return str(self.center_name)

class Ecrf(models.Model):
    ecrf_name = models.CharField(max_length=50)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date')
    theoritical_number_of_patients = models.CharField(max_length=50)

    def __unicode__(self):
        return str(self.ecrf_name)


