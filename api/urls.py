from django.urls import path, include, re_path
from rest_framework import routers
router = routers.DefaultRouter()
from .views import *

from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
router.register(r'devices', FCMDeviceAuthorizedViewSet)




urlpatterns = [
    path('auth/', obtain_auth_token, name='api_token_auth'),
    re_path(r'^', include(router.urls)),
    path('subjects/', SubjectView.as_view(), name="subjects"),
    path('chapters/<slug:slug>', ChapterView.as_view(), name="chapters"),
    path('documents/<slug:slug>', DocumentView.as_view(), name="documents"),
    path('videos/<slug:slug>', VideoView.as_view(), name="videos"),



]
