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
from lms_app.models import Syllabus, Standard, Subject, Chapter, Documents, Student
from fcm_django.models import FCMDevice
import requests
devices = FCMDevice.objects.all()




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


def get_video_url(vimeo_id):
	API_ENDPOINT = 'https://player.vimeo.com/video/'+vimeo_id+'/config'
	response = requests.get(url = API_ENDPOINT)
	return response.json().get('request').get('files').get('hls').get('cdns').get('akfire_interconnect_quic').get('url')


class SubjectView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        user = request.user
        user = get_user_model().objects.get(id=user.id)
        user = user.student
        try:
            subjects = user.scheme.subject.all()
            subjects = SubjectSerializer(subjects, many=True).data
            devices.send_message("subjects Fetched", "The subjects api fetched")
        except:
            subjects = []
        
        return Response({'subjects': subjects})


# class ChapterView(APIView):
#     permission_classes = (IsAuthenticated, )

#     def get(self, request, slug):
#         user = request.user
#         user = get_user_model().objects.get(id=user.id)
#         user = user.student
#         if user.is_paid == True:
#             try:
#                 subject = Subject.objects.get(slug=slug)
#                 chapters = subject.chapter_set.all()
            
#                 chapters = ChapterSerializer(chapters, many=True).data
#             except:
#                 chapters = []
#         elif user.is_paid == False:
#             try:
#                 subject = Subject.objects.get(slug=slug)
#                 chapters = subject.chapter_set.filter(free_tier=True)
            
#                 chapters = ChapterSerializer(chapters, many=True).data
#             except:
#                 chapters = []
#         else:
#             chapters = []
        
#         return Response({'chapters': chapters})


class ChapterView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, slug):
        user = request.user
        user = get_user_model().objects.get(id=user.id)
        student = user.student
        if student.is_paid == True:
            try:
                subject = Subject.objects.get(slug=slug,standard=student.standard)
                chapters = subject.chapter_set.all()
            
                chapters = ChapterSerializer(chapters, many=True).data
            except:
                chapters = []
        elif student.is_paid == False:
            try:
                subject = Subject.objects.get(slug=slug,standard=student.standard)
                chapters = subject.chapter_set.filter(free_tier=True)
            
                chapters = ChapterSerializer(chapters, many=True).data
            except:
                chapters = []
        else:
            chapters = []
        
        return Response({'chapters': chapters})


class DocumentView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, slug):
       
        
        try:
            chapter = Chapter.objects.get(slug=slug)
            documents = chapter.documents_set.all()
        
            documents = DocumentSerializer(documents, many=True).data
        except:
            documents = []
        
        return Response({'documents': documents})





def get_video_url(vimeo_id):
	API_ENDPOINT = 'https://player.vimeo.com/video/'+vimeo_id+'/config'
	response = requests.get(url = API_ENDPOINT)
	return response.json().get('request').get('files').get('progressive')[1].get("url")


class GetVimeo(APIView):

	def get(self, request):


		urls = get_video_url('35527420')

		context = {
			'feedbacks': urls
		}

		return Response(urls)

class VideoView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, slug):
       
        
        try:
            chapter = Chapter.objects.get(slug=slug)
            videos = chapter.video_set.all()
        
            videos = VideoSerializer(videos, many=True).data
        except:
            videos = []
        
        return Response({'videos': videos})


class DoubtView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, slug):
       
        
        try:
            chapter = Chapter.objects.get(slug=slug)
            videos = chapter.video_set.all()
        
            videos = VideoSerializer(videos, many=True).data
        except:
            videos = []
        
        return Response({'videos': videos})