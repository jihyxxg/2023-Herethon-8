from django.contrib import admin

from .models import Hospital, Review
# Register your models here.
class CommentInline(admin.TabularInline):
    model=Review
    verbose_name_plural = '댓글 입력 !'

@admin.register(Hospital)
class HospitalModelAdmin(admin.ModelAdmin):
    list_display=('name','content', 'created_at')
    search_fields=('name',)
    inlines=[CommentInline]
