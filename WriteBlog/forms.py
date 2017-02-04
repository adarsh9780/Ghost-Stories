from django import forms
from .models import BlogAuthor, BlogContent

class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogContent
        fields = ['title', 'text']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title

    def clean_text(self):
        text = self.cleaned_data.get('text')
        return text