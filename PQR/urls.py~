from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.list, name ='list_patient'),
    url(r'^(?P<patient_id>[0-9]+)/patient/$', views.detail2, name ='detail_patient'),
]
