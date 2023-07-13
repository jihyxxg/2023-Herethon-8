from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .forms import QuestionForm

def question_view(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id) #id에 해당하는 객체 get 
    context = {'question' : question} #위에서 get한 question 객체를 text화
    return render(request, 'question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone)
    return redirect('qnas:detail', question_id=question_id)

def question_create(request):
    form = QuestionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            qst = Question()
            qst.writer = form.cleaned_data['writer']
            qst.subject = form.cleaned_data['subject']
            qst.create_date = form.cleaned_data['create_date']
            qst.save()
            return redirect('http://127.0.0.1:8000/question_list')
        
        else:
            qst = QuestionForm()
    
    return render(request, 'question_write.html', {'form' : form})