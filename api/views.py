from rest_framework import generics, permissions
from learn.models import Question
from .serializers import QuestionSerializer 

class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
