from django.db import models


# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name + ' [' + str(self.id) + ']'
        
    def listReply(self):
        replies = Reply.objects.filter(patient= self.id)
        return replies

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text
    

class Reply(models.Model):
    question = models.ForeignKey(Question)
    patient = models.ForeignKey(Patient)
    reply_text = models.CharField(max_length=200)
    
    def __unicode__(self):
        return str(self.reply_text) 
        
