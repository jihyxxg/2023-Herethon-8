"""스마트여성병원서비스 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from qnas.views import question_view, detail, question_create
from qnas import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('hospitalapp.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('question_write/question_list/<str:username>/', question_view, name='mypage'),
    path('question_list/question/<int:question_id>/', views.detail, name='detail'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question_write/', views.question_create, name='question_write'),
    path('question_list/', views.question_view, name = 'question_view')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
