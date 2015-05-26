from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#-*- coding: utf-8 -*-


def index(request):
    return HttpResponse("Hello, world. You're at the Webtrial index.")

def detail(request, patient_id):
    return HttpResponse("You are looking at Patient %s." % patient_id)

def results(request, patient_id):
    response = "You're looking at the results of patient %s."
    return HttpResponse(response % patient_id)

def vote(request, patient_id):
    return HttpResponse("You're voting on question %s." % patient_id)

