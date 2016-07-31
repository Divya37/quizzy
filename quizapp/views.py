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
    return HttpResponse(render(request,'quizapp/home.html'))

def Evaluate_quiz(request, id):
    p = Question.objects.values_list().filter(id=id)
    template = loader.get_template('quizapp/result.html')
    res = template.render(p)
    return HttpResponse(res)

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from quizapp.forms import RegistrationForm

def get_registrationform(request):
    if(request.method=='POST'):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            if password1==password2:
                User.objects.create_superuser(username,email,password1)
                return HttpResponseRedirect("/")
            else:
                form=RegistrationForm()
        return render(request,'registration.html',{'form':RegistrationForm})
    else:
        return render(request,'registration.html',{'form':RegistrationForm})

def quiz(request):
    return render(request, "quizlist.html")
def questions(request):
    return render(request, "questionlist.html")