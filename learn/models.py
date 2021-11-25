from django.db import models
from django.urls import reverse

class Chapter(models.Model):
    title = models.CharField(max_length=100)
    slno = models.IntegerField(default=0)
    no_of_pages = models.IntegerField(default=0)
    scroll_height = models.FloatField(default=0.0)
    
    class Meta:
        ordering = ['slno']
        
    def get_absolute_url(self):
        return reverse("learn:chapter-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f"{self.title} ({self.no_of_pages})"

class Question(models.Model):
    rule = models.CharField(max_length=1000, default='')
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    page_no = models.IntegerField()

    is_bookmarked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question} | {self.chapter.title} ({self.corresponding_page_no})"


class PageComplition(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    page_number = models.IntegerField()

    def __str__(self):
        return f"{self.chapter.title} page {self.page_number} completed."