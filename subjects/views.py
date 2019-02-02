from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Subjects, Syllabus
class IndexView(generic.ListView):
    model = Subjects
    template_name = 'subjects/index.html'

def detail(request, subjects_id):
    return HttpResponse("You're looking at subject %s." % subjects_id)
def detail(request, subjects_id):
    subjects = get_object_or_404(Subjects, pk=subjects_id)
    return render(request, 'subjects/detail.html', {'subjects': subjects})
def results(request, subjects_id):
    response = "You're looking at the results of subject %s."
    return HttpResponse(response % subjects_id)

def vote(request, subjects_id):
    return HttpResponse("You're voting on subject %s." % subjects_id)
