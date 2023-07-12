from django.db import models

# Create your models here.
from users.models import User
# Create your models here.

class Hospital(models.Model): 
    CATEGORY=[
        ('서울특별시','서울특별시'),
        ('경기도','경기도'),
        ('인천광역시','인천광역시'),
        ('강원특별자치도','강원특별자치도'),
        ('대전광역시','대전광역시'),
        ('세종특별자치도','세종특별자치도'),
        ('충청남도','충청남도'),
        ('충청북도','충청북도'),
        ('부산광역시','부산광역시'),
        ('울산광역시','울산광역시'),
        ('경상남도','경상남도'),
        ('경상북도','경상북도'),
        ('대구광역시','대구광역시'),
        ('광주광역시','광주광역시'),
        ('전라남도','전라남도'),
        ('전라북도','전라북도'),
        ('제주특별자치도','제주특별자치도'),
    ]
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
    waiting=models.IntegerField(verbose_name="대기자수",default=0)
    created_at=models.DateTimeField(auto_now=True)
    where = models.CharField(verbose_name="병원 주소", default='', max_length=10, choices=CATEGORY)
    reservated_users = models.ManyToManyField(User, related_name='reservated_users',verbose_name="이 병원에 예약한 사용자")
    def increase_waiter(self):
        self.waiting+=1

class Review(models.Model):
    point=models.IntegerField(verbose_name="평점",null=True)
    title=models.CharField(max_length=20, null=True,verbose_name="제목")
    comment=models.TextField(verbose_name="내용")
    writer=models.CharField(max_length=20,null=True,verbose_name="작성자")
    hospital=models.ForeignKey(Hospital, on_delete=models.CASCADE,verbose_name="리뷰 대상 병원")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="생성일자") 