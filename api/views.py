from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
import json
import datetime
from django.conf import settings
# import requests
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.auth import get_user_model
from lms_app.models import Syllabus, Standard, Subject, Chapter


# class SyllabusView(ListAPIView):



# class SubjectView(APIView):
#     permission_classes = (IsAuthenticated, )

#     def get(self, request):
#         try:
#             subjects = Subject.objects.filter(active=True)
#             subjects = SubjectSerializer(subjects, many=True).data
#         except:
#             subjects = []
        
#         return Response({'subjects': subjects})




class SubjectView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        try:
            subjects = Subject.objects.filter(active=True)
            subjects = SubjectSerializer(subjects, many=True).data
        except:
            subjects = []
        
        return Response({'subjects': subjects})