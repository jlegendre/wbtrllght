from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.db.models import Prefetch
from .models import Patient, Question, Reply

# Create your views here.

def list(request):
	list_patient = Patient.objects.order_by('name')
	context = RequestContext(request, {
	    'list_patient':list_patient,
	    'welcome': 'Welcome on my page Django !',
	})
	return render(request, 'PQR/list.html', context)
	

def detail(request, patient_id):
    tab_replies = []
    patient = get_object_or_404(Patient, pk=patient_id)
    questions = Question.objects.all().order_by('pub_date')
    for question in questions:
        tab_replies.append(question.reply_set.filter(patient=patient_id))
    replies_per_question = zip(questions, tab_replies)    
    return render_to_response('PQR/detail.html', {'questions_list': replies_per_question, 'patient': patient })
    
    
    
    
    
    
    """def detail(request, patient_id, **kwargs):
    patient = get_object_or_404(Patient, pk=patient_id)
    list_question = Question.objects.all()
    Replies4MyPatient = Reply.objects.filter(patient=patient_id)
    return render(request, 'PQR/detail.html', locals())"""
