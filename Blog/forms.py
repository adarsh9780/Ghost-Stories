from django import forms


class BlogForm(forms.Form):
    
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=200)
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username
