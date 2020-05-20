from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
import datetime

# Create your views here.
def current_datetime(request):
    now =  datetime.datetime.now()
    html = "<html><body>It is %s now"%(now)
    return HttpResponse(200,html)

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)