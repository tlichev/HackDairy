# comments/forms.py
from django import forms

from HackDairy.comment.models import Comment
from HackDairy.themes.models import Theme


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['title', 'subtitle', 'content', 'banner_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'text': 'Коментар',
        }