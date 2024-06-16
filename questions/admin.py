from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    ordering=('id',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=('course','question','answer','options_one','options_two','options_three','options_four')
    list_filter=('course',)
    ordering=('course',)

@admin.register(ScoreBoard)
class ScoreBoardAdmin(admin.ModelAdmin):
    list_display=('user','course','score')
    list_filter=('user','course')
