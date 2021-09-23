from django.db import models
from django.utils.text import slugify 
from django.urls import reverse 
import os 

class Chapter(models.Model):
    title = models.CharField(max_length=200)
    slno = models.IntegerField()
    static_folder = models.SlugField(null=False)
    total_pages = models.IntegerField()
    last_read_page = models.IntegerField(default=1) 

    def save(self, *args, **kwargs):
        self.static_folder = slugify(self.title)
        try:
            os.mkdir(os.path.join('myapp', 'static', 'pages', slugify(self.title)+'test'))
            print(os.getcwd())
        except:
            pass 
        super().save(*args, **kwargs) 
    
    def get_absolute_url(self):
        return reverse("chapter-detail-page", kwargs={"pk": self.pk})
    

    def __str__(self):
        return f"Chapter: {self.slno} - {self.title} (Pages: {self.total_pages})"


class Question(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)
    page_number = models.IntegerField() 
    is_bookmarked = models.BooleanField(default=False)

    def __str__(self):
        return f"Chapter: {self.chapter.slno} - Quesiton: {self.question}"


class Practice(models.Model):
    no_of_question = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False) # true -> running and false -> ended or not started

    

    def __str__(self):
        return f"Test on {self.datetime} ({self.no_of_question})"

class TestQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test = models.ForeignKey(Practice, on_delete=models.CASCADE)
    student_answer = models.CharField(max_length=1000)
    status = models.IntegerField(default=0) # 0->not checked, 1->correct attempt, -1->incorrect attempt, 2->not attempt

    def staus_str(self):
        if self.status == 0:
            status = 'Not Checked'
        elif self.status == 1:
            status = 'Correct Attempt'
        elif self.status == -1:
            status = 'Inorrect Attempt'
        elif self.status == 2:
            status = 'Not Attempt'
        return status 

    def __str__(self):
        return f"{self.quesiton} - {self.staus_str()} - Test: {self.test.datetime}"


