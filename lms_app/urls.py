from django.contrib import admin
from django.urls import path
from . import views as lms_views



# app_name = "lms-app"

urlpatterns = [
    path('teacher/',lms_views.TeacherList.as_view(), name='teacher_list'),
    path('student/',lms_views.StudentList.as_view(), name='student_list'),
    path('syllabus/',lms_views.syllabus_list, name='syllabus_list'),
    path('syllabus/update/<int:pk>/',lms_views.syllabus_update, name='syllabus_update'),


    path('standard/', lms_views.standard_list, name='standard_list'),
    path('standard/update/<int:pk>/', lms_views.standard_update, name='standard_update'),
    
    path('subjects/',lms_views.subject_list, name='subject_list'),
    path('subjects/update/<int:pk>/',lms_views.subject_update, name='subject_update'),
    path('chapters/',lms_views.chapter_list, name='chapter_list'),
    path('chapters/update/<int:pk>/',lms_views.chapter_update, name='chapter_update'),
    path('scheme/',lms_views.scheme_list, name='scheme_list'),
    path('scheme/update/<int:pk>/',lms_views.scheme_update, name='scheme_update'),
    path('scheme_upload/',lms_views.scheme_upload, name='scheme_upload'),

    
    path('register_teacher/',lms_views.registepage, name='teacher'),
    path('teacher/update/<int:pk>/',lms_views.teacher_update, name='teacher_update'),
    path('register_student/',lms_views.studentpage, name='student'),
    path('student/update/<int:pk>/',lms_views.student_update, name='student_update'),
    path('videos_list/',lms_views.video_list, name='video'),
    path('video_up/',lms_views.file_upload, name='up'),
    path('video/update/<int:pk>/', lms_views.video_update, name='video_update'),
    path('document_list/',lms_views.upload_document.as_view(), name='document'),
    path('document_up/',lms_views.docs_upload, name='upload'),
    path('document/update/<int:pk>/', lms_views.docs_update, name='docs_update'),
    path('notification_list/',lms_views.Notification_list.as_view(), name='notify'),
    path('add_notification/',lms_views.notifi_up, name='addnotify'),
    path('notification/update/<int:pk>/',lms_views.notification_update, name='notification_update'),

    
    #path('profile_t/',lms_views.Profilep.as_view(), name='pro'),
    path('study_list/',lms_views.Upload_material.as_view(), name='studyfile'),
    path('study_up/',lms_views.study_upload, name='Supload'),
    path('study/update/<int:pk>/', lms_views.study_update, name='study_update'),
    path('Question/',lms_views.Question_Paper.as_view(), name='questions'),
    path('question_up/',lms_views.question_upload, name='question_up'),
    path('question/update/<int:pk>/', lms_views.question_update, name='question_update'),
    path('student_view/<int:pk>',lms_views.StudentView, name='studentview'),
    path('teacher_view/<int:pk>',lms_views.TeacherView, name='teacherview'),
    # path('comment/<int:pk>',lms_views.comments, name='commentadd'),
    path('comments/<int:pk>',lms_views.commenting, name='commentup'),


    path('toggle/', lms_views.toggle, name="toggle"),
    path('toggle_ispaid/', lms_views.toggle_ispaid, name="toggle_ispaid"),
    path('toggle_freetier/', lms_views.toggle_freetier, name="toggle_freetier"),

    
    path('ajax/load-standard/', lms_views.load_standard, name='ajax_load_std'),
    path('ajax/load-scheme/', lms_views.load_scheme, name='ajax_load_scheme'),
    path('ajax/load-subject/', lms_views.load_subject, name='ajax_load_subj'),
    path('ajax/load-chapter/', lms_views.load_chapter, name='ajax_load_chap'),
    path('ajax/load-country/', lms_views.load_country, name='ajax_load_con'),
    path('video_up/<int:pk>/', lms_views.chapter_video_upload, name='chapter_video_upload'),




# 'register_teacher/',register

    

]
