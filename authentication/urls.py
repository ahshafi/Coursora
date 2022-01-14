from django.urls import path

from authentication.views import *

app_name="authentication"
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/logout', logout, name='logout')
]