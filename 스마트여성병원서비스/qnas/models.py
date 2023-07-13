from django.db import models
from django.contrib.auth import get_user_model

#User = get_user_model()

#질문 모델
class Question(models.Model):
    subject = models.CharField(verbose_name='제목', max_length=200)
    content = models.TextField(verbose_name='내용')
    create_date = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    writer = models.TextField(verbose_name='작성자')
    
    #셸에서 모델 데이터 조회 시 각 객체의 제목을 출력하도록 함
    def __str__(self):
        return self.subject

#답변 모델
class Answer(models.Model):
    question = models.OneToOneField(Question, verbose_name='답변자', on_delete=models.CASCADE)
    #외래키 제약조건 무시하고 연쇄 삭제됨
    content = models.TextField(verbose_name='내용')
    create_date = models.DateTimeField(auto_now_add=True)
    writer = models.TextField(verbose_name='작성자')
