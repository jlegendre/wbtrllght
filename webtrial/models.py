from django.db import models

# Create your models here.
class Patient(models.Model):
    initials = models.CharField(max_length=50)
    status = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date published')
    modification_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return str(self.initials) + ' - ' + str(self.status)