from django.db import models

# Create your models here.
from users.models import User
# Create your models here.

class Hospital(models.Model): 
    woman=models.BooleanField(verbose_name="여자전문의",default=False)
    night_care=models.BooleanField(verbose_name="야간진료",default=False)
    saturday_treatment=models.BooleanField(verbose_name="토요일 진료",default=False)
    holiday_treatment=models.BooleanField(verbose_name="공휴일 진료",default=False)
    sunday_care=models.BooleanField(verbose_name="일요일 진료",default=False)
    latitude=models.FloatField(verbose_name="위도",default=0.0) #지도에 표시하기 위함 
    longtitude=models.FloatField(verbose_name="경도",default=0.0)
    name = models.CharField(verbose_name="병원 이름",max_length=30)  
    content=models.TextField(verbose_name="병원 소개 내용",null=True)
    adress=models.CharField(verbose_name="병원 주소",max_length=200)
    image=models.ImageField(verbose_name="병원 소개 이미지",upload_to='hospital/',default=None,null=True)
    created_at = models.DateTimeField(verbose_name="등록일자",auto_now_add=True)   #등록일자도 필요 없을 듯 해요
    waiting=models.IntegerField(verbose_name="대기자수",default=0)
    where=models.CharField(verbose_name="병원 주소 (시도구)",default=0,max_length=10)
    reservated_users = models.ManyToManyField(User, related_name='reservated_users',verbose_name="이 병원에 예약한 사용자")
    def increase_waiter(self): #예약하면 대기자 수 올리는 기능은 필요 없을 듯 합니다!
        self.waiting+=1

class Review(models.Model):
    title=models.CharField(max_length=20, null=True,verbose_name="리뷰제목")
    comment=models.TextField(verbose_name="리뷰내용")
    writer=models.CharField(max_length=20,null=True,verbose_name="리뷰 작성자")
    hospital=models.ForeignKey(Hospital, on_delete=models.CASCADE,verbose_name="리뷰 작성 대상 병원")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="리뷰 생성일") 