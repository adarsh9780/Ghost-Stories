from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import BlogForm


class IndexPage(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'Blog/index.html', {})

class AboutPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Blog/about.html", {})

class ContactPage(View):

    def get(self, request, *args, **kwargs):
        return render(request, "Blog/contact.html", {})