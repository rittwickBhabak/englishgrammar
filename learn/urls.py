from django.urls import path
from . import views

# ChapterList
# ChapterDetail
# EditChapter
# PageDetail
# get_question_list
# add_question
# edit_question
# delete_question


app_name = "learn"

urlpatterns = [
    path("chapters", views.ChapterList.as_view(), name="chapter-list"),
    path("chapter/<int:pk>", views.ChapterDetail.as_view(), name="chapter-detail"),
    path(
        "chapter/<int:chapter_pk>/page/<int:page_no>",
        views.PageDetail.as_view(),
        name="page-detail",
    ),
    path("edit-chapter/<int:pk>", views.EditChapter.as_view(), name="edit-chapter"),
    path("question-list", views.get_question_list, name="question-list"),
    path("add-question", views.add_question, name="add-question"),
    path("edit-question/<int:pk>/", views.edit_question, name="edit-question"),
    path("delete-question/<int:pk>/", views.delete_question, name="delete-question"),
    path("toggle-bookmark/<int:pk>/", views.toggle_bookmark, name="toggle-bookmark"),
    path("toggle-completion", views.toggle_completion, name="toggle-completion"),
]
