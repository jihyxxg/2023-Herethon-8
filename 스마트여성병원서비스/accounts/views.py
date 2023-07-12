from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .forms import UserCreateForm, SignUpForm
def signup_view(request):
    #get 요청 시 html 응답
    if request.method=='GET':
        form=SignUpForm
        context={'form':form}
        return render(request, 'accounts/signup.html',context)
    
    else:
        #post요청 시 데이터 확인 후 회원 생성
        form=SignUpForm(request.POST)
        if form.is_valid():  #ture면 회원가입처리
            instance=form.save()
            return redirect('index')

        else:  #flase이면 돌려버림 
            return redirect('signup')
        
def login_view(request):
    #get,post분리
    if request.method=='GET':
        #로그인 html 파일 응답 
        return render(request, 'accounts/login.html',{'form':AuthenticationForm()})
    else: 
        #데이터 유효성 검사
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid(): 
            #비즈니스 로직 처리 - 로그인 성공 - 로그인처리 
            login(request, form.user_cache)  #로그인 처리를 하는 함수
            #응답
            return redirect('index') #인덱스 페이지로 돌려보냄 
        else:
            #비즈니스 로직 처리 - 로그인 실패
            #응답
            return render(request, 'accounts/login.html',{'form':form})

def logout_view(request):
    #유효성 검사
    if request.user.is_authenticated:  #프로퍼티라고 설정되어 있어서 괄호 없어도 됨 
        #비즈니스 로직 처리-로그아웃
        logout(request)
    #응답 
    return redirect('index')