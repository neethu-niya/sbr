from django.contrib import admin
from django.urls import path
from . import views
from .views import syllabus_list, standard_list, subject_list, chapter_list, TeacherList, StudentList, registepage

urlpatterns = [
    path('teacher/',TeacherList.as_view(), name='teacher_list'),
    path('student/',StudentList.as_view(), name='student_list'),
    path('syllabus/',syllabus_list, name='syllabus_list'),
    path('standard/',standard_list, name='standard_list'),
    
    path('subjects/',subject_list, name='subject_list'),
    path('chapters/',chapter_list, name='chapter_list'),
    path('register_teacher/',views.registepage, name='teacher'),
    path('register_student/',views.studentpage, name='student'),
    path('videos_list/',views.upload_video.as_view(), name='video'),
    path('video_up/',views.file_upload, name='up'),
    path('document_list/',views.upload_document.as_view(), name='document'),
    path('document_up/',views.docs_upload, name='upload'),


    

# 'register_teacher/',register

    

]