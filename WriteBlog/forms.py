from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'text']

    def clean_author(self):
        author = self.cleaned_data.get('author')
        return author

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        return image

    def clean_text(self):
        text = self.cleaned_data.get('text')
        return text

    def clean_video(self):
        video = self.cleaned_data.get('video')
        return video