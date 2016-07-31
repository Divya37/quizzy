from django.conf.urls import url
import views
import listviews

urlpatterns = [
    url(r'^quizlist/$', listviews.Exams_view.as_view(), name= 'quiz_view'),
    url(r'^quizlist/(?P<pk>[0-9]+)/$', listviews.Questions_view.as_view(), name= 'detailed_view'),
    url(r'^quizlist/createquiz/$', listviews.Create_quiz.as_view()),
    url(r'^quizlist/(?P<pk>[0-9]+)/writetest/$', listviews.Write_quiz.as_view()),
    url(r'^quizlist/(?P<pk>[0-9]+)/writetest/results$', views.Evaluate_quiz),
    url(r'^quizlist/(?P<pk>[0-9]+)/create_question/$', listviews.Create_question.as_view()),
]