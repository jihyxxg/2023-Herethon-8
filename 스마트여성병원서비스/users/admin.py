from django.contrib import admin

# Register your models here.
from .models import User

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display=['username','is_doctor']