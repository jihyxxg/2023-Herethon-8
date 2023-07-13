from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from users.models import User
from .forms import QuestionForm
from hospitalapp.models import Hospital, Review

def question_view(request, username):
    question_list = Question.objects.order_by('-create_date')
    user = get_object_or_404(User, username=username)
    reservated_hospitals = user.reservated_users.all()
    reviews=Review.objects.filter(writer=user)
    print(reviews)
    context = {
        'question_list': question_list,
        'reservated_hospitals': reservated_hospitals,
        'user': user,
        'reviews':reviews,
    }
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
            qst.subject = form.cleaned_data['subject']
            qst.content=form.cleaned_data['content']
            qst.writer=request.user
        
            qst.save()
            return redirect('mypage',request.user)
        
        else:
            qst = QuestionForm()
    
    return render(request, 'question_write.html', {'form' : form})

def review_create(request, user):
    user = User.objects.get(username=user)
    reservated_hospitals = user.reservated_users.all()
    if request.method == "POST":
        hospital_id = request.POST.get('hospital')
        hospital = Hospital.objects.get(id=hospital_id)
        Review.objects.create(
            comment=request.POST.get('content'),
            point=request.POST.get('point'),
            hospital=hospital,  # Hospital 인스턴스 할당
            writer=request.user
        )
        return redirect('hospital-detail', hospital_id)
    
    return render(request, 'review_create.html', {'reservated_hospitals': reservated_hospitals})
