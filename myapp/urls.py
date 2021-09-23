from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.chapter_list, name='chapter-list-page'),
    path("<slug:slug>/<int:page_no>", views.chapter_detail, name='chapter-detail-page'),
    path("add-question", views.add_question),
    path("practice-tests", views.practice_test_list, name='practice-test-list')
]
