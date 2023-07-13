from django.db import models
#from womanapp.models import Hospital
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserMangager


# 장고 모델이 db로 처리 날릴 때 관리 (일반 유저, 슈퍼유저, 스테프 )
class UserManager(DjangoUserMangager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("이메일은 필수 값입니다.")

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',False)  #시스템에서 분기처리를 해줘야함. 이 값은 직접 만들어서 넣어줌 
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)  #시스템에서 분기처리를 해줘야함. 이 값은 직접 만들어서 넣어줌 
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(username, email, password, **extra_fields)
    
class User(AbstractUser):
    doctor_picture=models.ImageField(verbose_name='의사사진',null=True, upload_to='doctor_picture/', blank=True)
    total_posts = models.PositiveIntegerField(default=0)
    is_doctor = models.BooleanField(default=False)
    objects = UserManager()
    comment=models.CharField(null=True,max_length=20)

    def increase_total_posts(self):
        self.total_posts += 1
        self.save()