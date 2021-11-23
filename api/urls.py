from re import I
from django.urls import path
from . import views 

app_name = 'api'

urlpatterns = [
    path('all-questions', views.QuestionList.as_view(), name='all-questions'),
]
