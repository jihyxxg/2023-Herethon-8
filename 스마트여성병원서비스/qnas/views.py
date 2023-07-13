from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question,Answer
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from users.models import User
from .forms import QuestionForm
from hospitalapp.models import Hospital, Review

@login_required
def question_view(request, username):
    if request.user.is_doctor:
        question_list = Question.objects.order_by('-create_date')
    else:
        question_list = Question.objects.filter(writer=username).order_by('-create_date')
    user = get_object_or_404(User, username=username)
    reservated_hospitals = user.reservated_users.all()
    reviews=Review.objects.filter(writer=user)
    context = {
        'question_list': question_list,
        'reservated_hospitals': reservated_hospitals,
        'user': user,
        'reviews':reviews,
    }
    return render(request, 'question_list.html', context)

def mypage5(request, hospital_name,review_id ):
    # hospital_id=Hospital.objects.filter(name=hospital_name)
    # hospital=Hospital.objects.get(id=hospital_id)
    # user=User.objects.get(username=username)
    review=Review.objects.get(id=review_id)

    return render(request, 'mypage5.html',{'review':review})
    #review=Review.objects.filter(hospital=hospital_name.id)

def detail(request, question_id):
    question = Question.objects.get(id=question_id) #id에 해당하는 객체 get 
    if Answer.objects.filter(question=question):
        answer=Answer.objects.filter(question=question)[0]
        doctor=get_object_or_404(User, username=answer.writer)
        print(type(doctor))
        context = {'question' : question,'answer':answer,'doctor':doctor} #위에서 get한 question 객체를 text화
    else:
        context = {'question' : question,'answer':None}
    return render(request, 'question_detail.html', context)

def answer_create(request, question_id):
    request.user.increase_total_posts()
    question = get_object_or_404(Question, pk=question_id)
    Answer.objects.create(question=question, content=request.POST.get('content'), writer=request.user, create_date=timezone)
    return redirect('question-detail', question_id=question_id)

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

@login_required
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
        return redirect('mypage', request.user)

    return render(request, 'review_create.html', {'reservated_hospitals': reservated_hospitals})
