from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=50)
    length = models.PositiveIntegerField()
    no_of_questions = models.IntegerField(default=0)
    user = models.ForeignKey(User, default=None)
    # def __str__(self):
    #     return self.name

class Question(models.Model):
    text = models.CharField(max_length=80)
    correct = models.PositiveIntegerField()
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    exam = models.ForeignKey(Exam)

    def __unicode__(self):
        return self.text
