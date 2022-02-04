from django import apps
from django.urls import *

from exams.views import *

urlpatterns=[
    path('exam/<int:exam_id>/', exam, name='exam') ,
]
