from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import BlogForm
from .models import Blog

class ViewBlog(View):

    def get(self, request, *args, **kwargs):
        form = BlogForm()
        
        # if request.user.is_authenticated():
        blog = Blog.objects.all().order_by('-timestamp')

        context = {
            'form': form,
            'blog': blog,
        }
            # return render(request, 'WriteBlog/home.html', context)
            
        return render(request, 'WriteBlog/home.html', context)

    def post(self, request, *args, **kwargs):
         form = BlogForm(request.POST or None, request.FILES or None)
         if form.is_valid():
            instance = form.save(commit= False)
            instance.save()
            return HttpResponseRedirect("/home")

            
         if request.user.is_authenticated():
            blog = Blog.objects.all()

         context = {
            'blog': blog,
            'form': form,
         }

         return render(request, "WriteBlog/home.html", context)

class WriteBlog(View):

    def get(self, request, *args, **kwargs):
        form = BlogForm()
        context={
            'form': form,
        }

        return render(request, 'WriteBlog/write_blog.html', context)