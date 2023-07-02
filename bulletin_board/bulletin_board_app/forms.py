from django import forms
from .models import Post, Reply


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'upload']


class ReplyCreateForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']
