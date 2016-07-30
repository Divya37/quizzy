from django.contrib import admin

# Register your models here.
from quizapp.models import Exam, Question
admin.site.register([Exam, Question])