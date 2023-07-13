from django import forms
from .models import Question

class QuestionForm(forms.Form):
    subject = forms.CharField()
    writer = forms.CharField()
    content = forms.CharField()
    create_date = forms.DateField()