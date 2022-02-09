from django import apps
from django.urls import *

from exams.views import *

urlpatterns=[
    path('exam/<int:exam_id>/', exam, name='exam') ,
    path('exam/<int:exam_id>/addquestion', add_ques, name='add_ques') ,
]
