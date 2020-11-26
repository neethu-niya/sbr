from rest_framework import serializers
from lms_app.models import Syllabus, Standard, Subject, Chapter, Documents, Video
from user.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'


class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    standard = serializers.CharField(source='get_standard')
    class Meta:
        model = Subject
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'





class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

