from django.db import models
from django.conf import settings

class BlogAuthor(models.Model):
    
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class BlogContent(models.Model):
    author = models.ForeignKey(BlogAuthor, default=1, on_delete=models.CASCADE, related_name = 'blog')
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title