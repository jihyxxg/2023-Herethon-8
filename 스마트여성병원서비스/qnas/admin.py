from django.contrib import admin
from .models import Question, Answer

# @admin.register(Question)
# class PostModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'subject', 'content', 'writer', 'create_date']
#     list_filter = ['create_date',]
#     search_fields = ['id', 'writer__username']
#     search_help_text = '게시판 번호, 작성자 검색이 가능합니다'

# @admin.register(Answer)
# class PostModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'question', 'content', 'writer', 'create_date']
#     list_filter = ['create_date',]
#     search_fields = ['id', 'writer__username']
#     search_help_text = '게시판 번호, 작성자 검색이 가능합니다'

class AmswerInline(admin.TabularInline):
    model=Answer 
    verbose_name_plural = '댓글 입력 !'


@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display=('subject','content','writer')
    inlines=[AmswerInline]