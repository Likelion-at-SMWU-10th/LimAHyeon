
from django import forms
from .models import Diary

class DiaryModelForm (forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'body']
        