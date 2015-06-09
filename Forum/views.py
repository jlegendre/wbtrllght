from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
#from django.template.response import TemplateResponse
from django.views.generic import CreateView

from .models import Choice, Question, Patient, Reply
#from .forms import QuestionForm

class IndexView(generic.ListView):
    template_name = 'Forum/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
        pub_date__lte=timezone.now()).order_by('pub_date')[:5]

    def get_context_data(self, **kwargs):
         context = super(IndexView, self).get_context_data(**kwargs)
         context['patient_list'] = Patient.objects.filter()
         context['question_list']= Question.objects.all()
         context['reply_list']   = Reply.objects.filter(patient__name__startswith='')
         return context

class PatientView(generic.ListView):
    template_name = 'Forum/patientlist.html'
    context_object_name = 'latest_patient_list'

    def get_queryset(self):
        return Patient.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'Forum/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'Forum/results.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'Forum/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('Forum:results', args=(p.id,)))


all_models_dict = {
    "template_name": "Forum/tous.html",
    "queryset": Question.objects.all(),
    "extra_context": {"choice_list": Choice.objects.all(),
                      "reply_list": Reply.objects.all(),
                     }
}



"""
class QuestionCreateView(CreateView):
    template_name = 'question_add.html'
    model = Question
    form_classe = QuestionForm
    success_url ='success/'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        choice_form = ChoiceFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  Choice_form=Choice_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        choice_form = ChoiceFormSet(self.request.POST)
        if (form.is_valid() and choice_form.is_valid() and
            choice_form.is_valid()):
            return self.form_valid(form, choice_form)
        else:
            return self.form_invalid(form, choice_form)


    def form_valid(self, form, choice_form):
        self.object = form.save()
        choice_form.instance = self.object
        choice_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, choice_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  choice_form=choice_form))"""
