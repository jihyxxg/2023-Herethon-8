from django.urls import path
from .views import *

urlpatterns=[
    path('',index, name='index'),
    path('hospital-detail/<int:hospital_id>',hospital_detail,name='hospital-detail'),
    path('hospital-detail/reservation/<int:hospital_id>',reservation, name='reservation'),
    path('hospital/<int:hospital_id>/review/create/',review_create, name='review-create')
]