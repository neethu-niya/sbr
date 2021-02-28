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


def get_video_url(vimeo_id):
	API_ENDPOINT = 'https://player.vimeo.com/video/'+vimeo_id+'/config'
	response = requests.get(url = API_ENDPOINT)
	return response.json().get('request').get('files').get('progressive')[1].get("url")


class VideoSerializer(serializers.ModelSerializer):

    vimeo_url = serializers.SerializerMethodField()

    def get_vimeo_url(self, obj):
        return get_video_url(obj.subtitle)


    class Meta:
        model = Video
        fields = ('name', 'subtitle', 'description', 'syllabus', 'standard', 'subject', 'chapter', 'image', 'thumbnail_image', 'vimeo_url')

        




