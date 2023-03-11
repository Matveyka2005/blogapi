from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "body", "created_at", "uploaded_at")
    list_display_links = ("title", "author")


admin.site.register(Post, PostAdmin)
