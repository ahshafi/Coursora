from django.urls import *

from courses.views import *


urlpatterns = [
    path('', show_course_list, name='show_course_list'),
    #path('contentlist/', show_content_list, name='show_content_list')
    path('contentlist/<int:course_id>/',show_content_list, name='show_content_list'),
    path('contentlist/<int:course_id>/view/<int:lec_id>',show_content_view, name='show_content_view'),
    path('contentlist/<int:course_id>/reg/',course_reg, name='course_reg')   
]