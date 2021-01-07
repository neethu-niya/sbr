from django.contrib import admin
from django.urls import path
from . import views
from .views import (
    syllabus_list, standard_list, subject_list, chapter_list, TeacherList,
    StudentList, registepage, Notification_list, Upload_material , Question_Paper ,
    StudentView, toggle, scheme_list, toggle_ispaid, toggle_freetier
)


# app_name = "lms-app"

urlpatterns = [
    path('teacher/',TeacherList.as_view(), name='teacher_list'),
    path('student/',StudentList.as_view(), name='student_list'),
    path('syllabus/',syllabus_list, name='syllabus_list'),
    path('standard/',standard_list, name='standard_list'),
    
    path('subjects/',subject_list, name='subject_list'),
    path('chapters/',chapter_list, name='chapter_list'),
    path('scheme/',scheme_list, name='scheme_list'),
    path('scheme_upload/',views.scheme_upload, name='scheme_upload'),

    
    path('register_teacher/',views.registepage, name='teacher'),
    path('register_student/',views.studentpage, name='student'),
    path('videos_list/',views.video_list, name='video'),
    path('video_up/',views.file_upload, name='up'),
    path('video/update/<int:pk>/', views.video_update, name='video_update'),
    path('document_list/',views.upload_document.as_view(), name='document'),
    path('document_up/',views.docs_upload, name='upload'),
    path('notification_list/',views.Notification_list.as_view(), name='notify'),
    path('add_notification/',views.notifi_up, name='addnotify'),
    #path('profile_t/',views.Profilep.as_view(), name='pro'),
    path('study_list/',views.Upload_material.as_view(), name='studyfile'),
    path('study_up/',views.study_upload, name='Supload'),
    path('Question/',views.Question_Paper.as_view(), name='questions'),
    path('question_up/',views.question_upload, name='question_up'),
    path('student_view/<int:pk>',views.StudentView, name='studentview'),
    path('teacher_view/<int:pk>',views.TeacherView, name='teacherview'),
    # path('comment/<int:pk>',views.comments, name='commentadd'),
    path('comments/<int:pk>',views.commenting, name='commentup'),


    path('toggle/', toggle, name="toggle"),
    path('toggle_ispaid/', toggle_ispaid, name="toggle_ispaid"),
    path('toggle_freetier/', toggle_freetier, name="toggle_freetier"),

    
    path('ajax/load-standard/', views.load_standard, name='ajax_load_std'),
    path('ajax/load-scheme/', views.load_scheme, name='ajax_load_scheme'),
    path('ajax/load-subject/', views.load_subject, name='ajax_load_subj'),
    path('ajax/load-chapter/', views.load_chapter, name='ajax_load_chap'),
    path('ajax/load-country/', views.load_country, name='ajax_load_con'),
    path('video_up/<int:pk>/', views.chapter_video_upload, name='chapter_video_upload'),




# 'register_teacher/',register

    

]
