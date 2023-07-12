from django.shortcuts import render,redirect,get_object_or_404
from .models import Hospital, Review
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Avg
# Create your views here.

def index(request):
    hospitals = Hospital.objects.all().annotate(reviews_count=Count('review')).annotate(average_point=Avg('review__point'))
    where = request.GET.get('where')
    title = request.GET.get('title')
    grade = request.GET.get('grade')
    night_care = request.GET.get('night_care')
    saturday_treatment = request.GET.get('saturday_treatment')
    holiday_treatment = request.GET.get('holiday_treatment')
    sunday_care = request.GET.get('sunday_care')
    woman = request.GET.get('woman')
    all=request.GET.get('all')
    if all:
        hospitals = hospitals.filter(night_care=True,saturday_treatment=True,holiday_treatment=True,sunday_care=True,woman=True)
    
    #추가로 넣어야 함 
    where_list = ['서울', '대구', '경기', '부산']
    default_grade = 0

    if night_care:
        hospitals = hospitals.filter(night_care=True)
    if saturday_treatment:
        hospitals = hospitals.filter(saturday_treatment=True)
    if holiday_treatment:
        hospitals = hospitals.filter(holiday_treatment=True)
    if sunday_care:
        hospitals = hospitals.filter(sunday_care=True)
    if woman:
        hospitals = hospitals.filter(woman=True)
    
    if grade in ['1', '2', '3', '4']:
        default_grade = int(grade)

    if where in where_list:
        hospitals = hospitals.filter(where=where)
    if title:
        hospitals = hospitals.filter(name__contains=title)
    if default_grade > 0:
        hospitals = hospitals.filter(average_point__gte=default_grade)

    return render(request, 'index.html', {'hospitals': hospitals, 'default_grade': default_grade})

def hospital_detail(request, hospital_id):
    hospital=get_object_or_404(Hospital, id=hospital_id)
    reviews = Review.objects.filter(hospital=hospital).all()
    if request.method=="POST":
        Review.objects.create(
            title=request.POST.get('title'),
            comment=request.POST.get('content'),
            point=request.POST.get('point'),
            hospital=hospital,
            writer=request.user
        )
        hospital.reservated_users.remove(request.user)
    return render(request, 'hospital/hospital_detail.html', {'hospital': hospital, 'reviews': reviews})


@login_required
def reservation(request,hospital_id):
    hospital= get_object_or_404(Hospital, id=hospital_id)
    reviews = Review.objects.filter(hospital=hospital).all()
    if request.method=="POST":
        hospital.increase_waiter()
        hospital.reservated_users.add(request.user)

        return render(request, 'hospital/hospital_detail.html', {'hospital': hospital, 'reviews': reviews,'errors':'','finish':'예약완료'})
