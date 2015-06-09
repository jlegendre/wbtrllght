import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.

TYPE_CHOICES = (
    ('radio', 'Radio'),
    ('text', 'Varchar'),      
)
class Patient(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    type = models.CharField(max_length=50, default='', choices=TYPE_CHOICES)

    def __unicode__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.choice_text

class Reply(models.Model):
    question = models.ForeignKey(Question)
    patient = models.ForeignKey(Patient)
    reply_text = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.reply_text
    
class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date',]

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text',]










