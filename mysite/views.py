from django.views.generic import TemplateView
import random
from learn.models import Question 

class HomePage(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = set(Question.objects.all())
        if len(questions) < 10:
            context["question_list"] = questions
        else:
            context["question_list"] = random.sample(set(Question.objects.all()), 10)
        return context
    