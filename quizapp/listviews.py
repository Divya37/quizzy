from django.http import HttpResponse
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator

from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.http import *
from models import *

class LoginRequiredMixin(object):
    u"""Ensures that user must be authenticated in order to access view."""
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class Exams_view(LoginRequiredMixin, ListView):
    model = Exam
    context_object_name = 'quiz_view'

class Questions_view(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'quizapp/exam_detail.html'

    def render_to_response(self, context, **response_kwargs):
        context.update({'object_list':Question.objects.filter(exam_id=int(self.kwargs.get('pk')))})
        return super(Questions_view, self).render_to_response(context, **response_kwargs)

    def get_queryset(self):
        q = Question.objects.all()
        return q

class Create_quiz(LoginRequiredMixin, CreateView):
    model = Exam
    fields = ['name', 'length', 'no_of_questions']
    def form_valid(self, form):
        list_form = form.save(commit=False)
        list_form.user = self.request.user
        list_form.save()
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return reverse('quiz_view')

class Create_question(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['text', 'correct', 'option1', 'option2', 'option3', 'option4']
    def form_valid(self, form):
        item_form = form.save(commit=False)
        item_form.exam_id = self.kwargs.get('pk')
        item_form.save()
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return reverse('detailed_view', kwargs={'pk': self.kwargs.get('pk')})

class Write_quiz(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'quizapp/test.html'

    def render_to_response(self, context, **response_kwargs):
        context.update({'object_list': Question.objects.filter(exam_id=int(self.kwargs.get('pk')))})
        return super(Write_quiz, self).render_to_response(context, **response_kwargs)

    def get_queryset(self):
        q = Question.objects.all()
        return q

    def get_object(self, queryset=None):
        return Question.objects.get(self.kwargs.get('pk'))

    def post(self,request,pk):
        user_ans = request._post
        ans = Question.objects.all().filter(exam_id=int(pk)).values_list('id','correct')
        ans=dict(ans)
        user_ans=dict((int(key[6:]),int(value)) for key,value in user_ans.items() if 'option' in key)
        count=0
        if len(list(ans)) ==0:
            return HttpResponse('result.html')
        for i in user_ans:
            if i in ans:
                if user_ans.get(i)==ans.get(i):
                    count+=1
        if request.method == "GET":
            return HttpResponse('test.html')
        else:
            return HttpResponse(render(request,'quizapp/answers.html',context={'count':count}))