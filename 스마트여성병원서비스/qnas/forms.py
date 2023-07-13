from django import forms
from .models import Question

class QuestionForm(forms.Form):
    subject = forms.CharField()
    content = forms.CharField()