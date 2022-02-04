from django import apps
from django.urls import *

from forums.views import *

urlpatterns = [
    path('forum/<int:forum_id>/', forum, name='forum'),
    
]