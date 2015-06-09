from django import forms
from .models import Question, Choice

class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=200)
    pub_date = forms.DateTimeField('date published')

class ChoiceForm(forms.Form):
    choice_text = forms.CharField(max_length=200)
    questions = forms.ModelMultipleChoiceField(queryset=Question.objects.all())
