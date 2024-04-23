from django.contrib import admin
from .models import Question
from .models import Option

# Register your models here.

class OptionInline(admin.TabularInline):  # Inline to display options with questions
    model = Option
    extra = 4  # Number of extra option fields to display


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]  # Add the OptionInline to the QuestionAdmin
    list_display = (
        'id',
        'text',
        'explanation',
        'photo_main',
        'category_id',


    )

class OptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'question_id',
        'question',
        'text',
        'is_correct',
    )
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
