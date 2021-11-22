from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Chapter, Question, Practice, TestQuestion

# Create your views here.
def chapter_list(request):
    context = {"chapters": Chapter.objects.all().order_by('slno')}
    return render(request, "myapp/chapter_list.html", context=context)


def chapter_detail(request, slug, page_no):
    chapter = get_object_or_404(Chapter, static_folder=slug)

    if chapter.total_pages < page_no:
        page_no = 1
    next_page_no = page_no + 1
    prev_page_no = page_no - 1
    if prev_page_no <= 0:
        prev_page_no = 1

    context = {
        "chapter": chapter,
        "questions": Question.objects.filter(
            chapter=chapter, page_number=page_no
        ).order_by("-id"),
        "page_no": page_no,
        "first_page": page_no == 1,
        "last_page": chapter.total_pages == page_no,
        "next_page_no": next_page_no,
        "prev_page_no": prev_page_no,
    }
    # chapter.last_read_page = int(page_no)
    # chapter.save()
    return render(request, "myapp/chapter_detail.html", context=context)


def add_question(request):
    if request.method == "POST":
        question = request.POST.get("question")
        answer = request.POST.get("answer")
        page_no = request.POST.get("page_no")
        chapter_pk = request.POST.get("chapter_pk")
        chapter = Chapter.objects.filter(id=chapter_pk).first()
        if chapter:
            q = Question.objects.create(
                question=question, answer=answer, chapter=chapter, page_number=page_no
            )
            return JsonResponse({"status": "success"})


def set_practice_test(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "myapp/set_practice_test.html")


def practice_test_list(request):
    context = {"tests": Practice.objects.all()}
    return render(request, "myapp/practice_test_list.html", context=context)
