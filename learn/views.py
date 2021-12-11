from django import urls
from django.db.models import query_utils
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView, TemplateView
from .models import Chapter, Question, PageComplition
from django.http import JsonResponse 
from django.contrib import messages
import json

class ChapterList(ListView):
    model = Chapter 

class ChapterDetail(DetailView):
    model = Chapter 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chapter = get_object_or_404(Chapter, pk=self.kwargs['pk'])
        context["question_list"] = Question.objects.filter(chapter=chapter)
        # context["page_url_list"] = [f"https://raw.githubusercontent.com/my-personal-repos/english-grammar-book/main/chapter-{chapter.slno}/{page}.jpg" for page in range(1, chapter.no_of_pages + 1)]
        context["page_number_list"] = [(page_number, chapter.pk) for page_number in range(1, chapter.no_of_pages + 1)]
        return context
    
class EditChapter(UpdateView):
    model = Chapter 
    fields = "__all__"

class PageDetail(TemplateView):
    template_name = 'learn/page_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chapter_pk"] = self.kwargs['chapter_pk']
        context["page_no"] = self.kwargs['page_no']
        chapter = get_object_or_404(Chapter, pk=self.kwargs['chapter_pk'])
        page_complition = PageComplition.objects.filter(chapter=chapter, page_number=self.kwargs['page_no']).first()
        if page_complition:
            context["is_completed"] = True
        else:
            context["is_completed"] = False
        if chapter.no_of_pages == self.kwargs['page_no']:
            next_page = 1
        else:
            next_page = int(self.kwargs['page_no']) + 1

        if self.kwargs['page_no'] == 1:
            prev_page = chapter.no_of_pages
        else:
            prev_page = int(self.kwargs['page_no']) - 1
        context["next_page"] = next_page
        context["prev_page"] = prev_page
        context["chapter"] = chapter
        context["question_list"] = Question.objects.filter(chapter=chapter, page_no=self.kwargs['page_no']).order_by('-pk')
        return context
    
def get_question_list(request, chapter_pk, page_no):
    chapter = get_object_or_404(Chapter, pk=chapter_pk)
    question_list = Question.objects.filter(chapter=chapter, page_no=page_no)
    return JsonResponse({"question_list": json.dumps(question_list)})


def add_question(request):
    if request.method == 'POST':
        rule = request.POST.get('rule').strip()
        question = request.POST.get('question').strip()
        answer = request.POST.get('answer').strip()
        chapter_pk = request.POST.get('chapter_pk')
        page_no = request.POST.get('page_no')

        chapter = Chapter.objects.filter(pk=chapter_pk).first()
        if chapter and chapter.no_of_pages>int(page_no):
            if len(question) > 0 and len(answer) > 0:
                Question.objects.create(question=question, answer=answer, rule=rule, chapter=chapter, page_no=page_no)
                messages.success(request, 'Question added successfully')
                return redirect(reverse('learn:page-detail', args=[chapter_pk, page_no]))
            else:
                messages.error(request, 'Some error occoured')
                return redirect(reverse('learn:page-detail', args=[chapter_pk, page_no]))
        else:
            messages.error(request, 'Some error occoured')
            return redirect(reverse('learn:page-detail', args=[chapter_pk, page_no]))    
    else:
        return render(request, "403.html", status=403)


def edit_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        rule = request.POST.get('rule').strip()
        question = request.POST.get('question').strip()
        answer = request.POST.get('answer').strip()
        question_pk = request.POST.get('question_pk')

        try:
            question_obj= get_object_or_404(Question, pk=int(question_pk))
            page_no = question_obj.page_no
            chapter_pk = question_obj.chapter.pk
            if len(question) > 0 and len(answer) > 0:
                question_obj.question = question
                question_obj.answer = answer
                question_obj.rule = rule
                question_obj.save()
                messages.success(request, 'Question Edited Successfully')
                return redirect(reverse('learn:page-detail', args=[chapter_pk, page_no]))
            else:
                messages.success(request, 'Question and Answer both are required')
                return redirect(reverse('learn:page-detail', args=[chapter_pk, page_no]))
        except:
            messages.success(request, 'Question not found')
            return redirect(reverse('learn:page-detail', args=[chapter_pk, page_no]))
    else:
        return render(request, "learn/question_form.html", {"question": question})


def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        chapter_pk = question.chapter.pk
        page_no = question.page_no
        question.delete()
        return redirect(reverse('learn:page-detail', args=[chapter_pk, page_no]))
    else:
        return render(request, "learn/question_confirm_delete.html", {"question": question})


def toggle_bookmark(request, pk):
    question = get_object_or_404(Question, pk=pk)

    question.is_bookmarked = not question.is_bookmarked
    question.save()
    return redirect(reverse('learn:page-detail', args=[question.chapter.pk, question.page_no]))

def toggle_completion(request):
    if request.method == 'POST':
        page_no = request.POST.get('page_no')
        chapter_pk = request.POST.get('chapter_pk')
        chapter = get_object_or_404(Chapter, pk=chapter_pk)
        obj = PageComplition.objects.filter(page_number=page_no, chapter=chapter).first()
        if obj is not None:
            obj.delete()
        else:
            PageComplition.objects.create(chapter=chapter, page_number=page_no)

        return redirect(reverse('learn:page-detail', args=[chapter_pk, page_no]))


def scroll_height(request):
    if request.method == "POST":
        s_height = request.POST.get('s_height')
        c_pk = request.POST.get('c_pk')

        chapter = get_object_or_404(Chapter, pk=int(c_pk))
        chapter.scroll_height = s_height 
        chapter.save()
        return JsonResponse({"status": "true", "message": "height updated"})
    else:
        return HttpResponse("Hi, You are cheating. ;-)")