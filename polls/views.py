from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
import datetime

# Create your views here.
def current_datetime(request):
    now =  datetime.datetime.now()
    html = "<html><body>[time]: %s"%(now)
    return HttpResponse(html, status=200)


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = Question.objects.filter(id=question_id)
    if not question:
        return JsonResponse({},status=404)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = Question.objects.filter(id=question_id)
    if not question:
        return JsonResponse({},status=404)
    
    choice = request.data.get('choice')
    if not choice:
        return JsonResponse({}, status=400)

    selected = question.choice_set.get(pk=choice)
    if not selected:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Choice Error",
        })

    selected.votes += 1
    selected.save()
    
    return HttpResponseRedirect(reverse('polls:results', args=(question.id)))


def results(request, question_id):
    question = Question.objects.filter(id=question_id)
    if not question:
        return JsonResponse({},status=404)
    
    return render(request, 'polls/results.html', {'question':question})