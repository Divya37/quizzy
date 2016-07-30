from django.shortcuts import render

# Create your views here.
from django.db.migrations import loader
from django.template import loader
from quizapp.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

def questionslist(request, id):
    items = Exam.objects.values_list().filter(id=id)
    template = loader.get_template('questionlist.html')
    res = template.render(context = {'questions':items})
    return HttpResponse(res)

def home(request):
    # template = loader.get_template('quizapp/home.html')
    return HttpResponse(render(request,'quizapp/home.html'))

def Evaluate_quiz(request, id):
    p = Question.objects.values_list().filter(id=id)
    template = loader.get_template('quizapp/result.html')
    res = template.render(p)
    return HttpResponse(res)

def quiz(request):
    return render(request, "quizlist.html")
def questions(request):
    return render(request, "questionlist.html")