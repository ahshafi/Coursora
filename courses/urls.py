from django import apps
from django.urls import *

from courses.views import *

app_name = 'courses'
urlpatterns = [
    path('courselist/', show_courselist, name='show_courselist'),
    #path('contentlist/', show_content_list, name='show_content_list')
    path('courselist/<int:course_id>/contentlist/',show_contentlist, name='show_contentlist'),
    path('courselist/<int:course_id>/contentlist/<int:lec_id>/view/',show_content_view, name='show_content_view'),
    path('courselist/<int:course_id>/reg/',course_reg, name='course_reg'),   
    path('add_course/', add_course, name='add_course'),
     
]