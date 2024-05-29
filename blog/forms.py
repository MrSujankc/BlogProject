from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        pass


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
