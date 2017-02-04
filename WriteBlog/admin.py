from django.contrib import admin
from .models import BlogAuthor, BlogContent

admin.site.register(BlogAuthor)
admin.site.register(BlogContent)