from django import forms
from django.forms.models import ModelForm
from .models import Category, Post


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','parent')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

#separate post form specifically for the header bar/homepage
class PostHomeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'category')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }