from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import BlogForm
from .models import BlogContent, BlogAuthor

class ViewBlogPage(View):

    def get(self, request, *args, **kwargs):
        form = BlogForm()
        # {
        # '''use below logic when particular user wants to see only his post'''
        #     blogauthor = BlogAuthor.objects.filter(name=request.user)
        #     blogcontent = blogauthor.blogcontent_set.all().order_by('-timestamp')
        # }
        blogcontent = BlogContent.objects.all().order_by('-timestamp')

        context = {
            'blogcontent': blogcontent,
            'form': form,
        }
            
        return render(request, 'WriteBlog/home.html', context)

    def post(self, request, *args, **kwargs):
        form = BlogForm(request.POST or None, request.FILES or None)
        # blogauthor = BlogAuthor(name=request.user)
        # if request.user == blogauthor:
        #     pass
        # else:
        #     blogauthor = BlogAuthor(name=request.user)
        #     blogauthor.save()
        # blogcontent = BlogContent.objects.all().order_by('-timestamp')

        if form.is_valid():
            instance = form.save(commit=False)
            # blogauthor = BlogAuthor.objects.filter(name=request.user)
            # blogcontent = BlogContent()
            # blogcontent.author = blogauthor
            # blogcontent.title = instance.title
            # blogcontent.text = instance.text
            # blogcontent.save()
            instance.save()
            return HttpResponseRedirect("/WriteBlog/home")

        context = {
            'blogcontent': blogcontent,
            'form': form,
        }

        return render(request, "WriteBlog/home.html", context)

class WriteBlogPage(View):

    def get(self, request, *args, **kwargs):
        form = BlogForm()
        context={
            'form': form,
        }

        return render(request, 'WriteBlog/write_blog.html', context)