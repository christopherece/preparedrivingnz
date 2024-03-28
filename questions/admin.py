from django.contrib import admin
from .models import Question
from .models import Option

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'explanation',
        'photo_main',
        'category_id',


    )
admin.site.register(Question, QuestionAdmin)

class OptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'question_id',
        'question',
        'text',
        'is_correct',
    )
admin.site.register(Option, OptionAdmin)