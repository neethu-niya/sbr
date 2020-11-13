from django.urls import path, include, re_path
from .views import *

from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

from rest_framework import routers
router = routers.DefaultRouter()


urlpatterns = [
    path('auth/', obtain_auth_token, name='api_token_auth'),
    path('subjects/', SubjectView.as_view(), name="subjects"),
    
]
