from django.contrib import admin
from .models import Chapter, Question, Practice, TestQuestion

# Register your models here.


class ChapterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"static_folder": ("title",)}


admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Question)
admin.site.register(Practice)
admin.site.register(TestQuestion)
