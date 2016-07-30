import sys
import os, django

sys.path.append("C:\summer\myquizapp")
os.environ['DJANGO_SETTINGS_MODULE'] = 'myquizapp.settings'
django.setup()

#college queries
from quizapp.models import *
count = 0
p = Exam.objects.values_list().filter(id=1)[0][0]
for i in Question.objects.values().filter(exam_id = p):
    for j in list(i):
        if j[:len(j)-1] == 'option':
            pass

print Question.objects.values()