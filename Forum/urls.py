from django.conf.urls import url
from .import views

urlpatterns = [   
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^patient$', views.PatientView.as_view(), name ='patient'),
    #url(r'^formulaire$', views.QuestionCreateView.as_view(), name ='question'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	#url(r'^$',list_detail.object_list, all_models_dict),
]
