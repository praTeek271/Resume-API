from django.contrib import admin
from .models import user_data

# Register your models here.

# admin.site.register(user_data)


@admin.register(user_data)

class User_data(admin.ModelAdmin):
    list_display=['username', 'selected','email', 'DOB','gender','state','resume']
    list_display_links=[ 'username', 'selected','email', 'DOB','gender','state','resume']
    list_filter=['selected','gender','state']
    list_per_page=5
