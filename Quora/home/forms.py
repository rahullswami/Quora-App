from django import forms
from .models import *

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write your answer here...'}),
        }


class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ['name', 'description']
        widgets = {
            'name': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Write your spaces here...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write your description here...'}),
        }