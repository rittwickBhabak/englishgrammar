from re import I
from django.urls import path
from . import views 

app_name = 'api'

urlpatterns = [
    path('random/1', views.Random1Question.as_view(), name='random-question'),
]
