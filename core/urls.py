# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'), name='api'),

    path("", include("authentication.urls")),  # add this
    path("", include("app.urls")),  # add this
    path("dashboard/", include("lms_app.urls")),
    path("select2/", include("django_select2.urls")),
    # path("search/", include("lms_app.urls")),


] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)