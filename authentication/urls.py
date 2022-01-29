from django.urls import path

from authentication.views import *

app_name="authentication"
urlpatterns = [
    path('',home,name='home'),
    path('login/', login, name='login'),
    path('register_student/', register_student, name='register_student'),
    path('register_teacher/', register_teacher, name='register_teacher'),
    path('profile/', profile, name='profile'),
    path('profile/logout', logout, name='logout')
]