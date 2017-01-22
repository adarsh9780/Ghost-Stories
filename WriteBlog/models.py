from django.db import models
from django.conf import settings

class Blog(models.Model):
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title
