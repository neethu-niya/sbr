from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Syllabus, Standard, Subject, Chapter, Teacher, Student
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from lms_app.forms import SyllabusForm, StandardForm, SubjectForm, ChapterForm, TeacherRegForm, StudentRegister, Comments_Form
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.http import HttpResponse
from django.http import JsonResponse
from fcm_django.models import FCMDevice
devices = FCMDevice.objects.all()

# from lms_app.functions.functions import handle_uploaded_file

@staff_member_required
def syllabus_list(request):
    syllabus = Syllabus.objects.all()
    form = SyllabusForm(request.POST or None)
    if form.is_valid():

        form.save()
        return redirect('syllabus_list')
    context = {'syllabus': syllabus, 'form': form}
    return render(request, 'lms_app/syllabus_list.html', context)

# def post_add_tags(request, pk):
#     post= get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = TagForm(request.POST)
#         if form.is_valid():
#             tag = form.save(commit=False) 
#             tag.post= post
#             tag.save()
#             return redirect("single_post_view", pk=post.pk)
#     else:
#         form = TagForm()
#     return render(request, "add_tags.html", {"form": form})

@staff_member_required
def standard_list(request):
    syllabus = request.GET.get('syllabus', None)
    standards = Standard.objects.all()
    if syllabus is not None:
        standards = standards.filter(syllabus__id__exact=syllabus)
    
    form = StandardForm(request.POST or None)
    if form.is_valid():
        form.cleaned_data
        form.save()
        return redirect('standard_list')
    context = {'standards': standards, 'form': form}
    return render(request, 'lms_app/standard_list.html', context)

@staff_member_required
def subject_list(request):
    standard = request.GET.get('standard', None)
    subjects = Subject.objects.all()
    if standard is not None:
        subjects = subjects.filter(standard__id__exact=standard)
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.cleaned_data
        form.save()
        return redirect('subject_list')
    context = {'subjects': subjects, 'form': form}
    return render(request, 'lms_app/subject_list.html', context)

@staff_member_required
def chapter_list(request):
    subject = request.GET.get('subject', None)
    chapters = Chapter.objects.all()
    if subject is not None:
        chapters = chapters.filter(subject__id__exact=subject)
    form = ChapterForm(request.POST or None)
    if form.is_valid():
        form.cleaned_data
        form.save()
        return redirect('chapter_list')
    context = {'chapters': chapters, 'form': form}
    return render(request, 'lms_app/chapter_list.html', context)


@staff_member_required
def scheme_list(request):
    subject = request.GET.get('subject')
    schemes = Scheme.objects.all()
    if subject is not None:
        schemes = schemes.filter(subject__id__exact=subject)
    form = SchemeForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.cleaned_data
        form.save()
        return redirect('scheme_list')
    context = {'schemes': schemes, 'form': form}
    return render(request, 'lms_app/scheme_list.html', context)




class TeacherList(ListView):
    queryset = Teacher.objects.all()
    context_object_name = 'teachers'
    template_name = 'lms_app/teacher_list.html'

def TeacherView(request, pk):
    teachers = get_object_or_404(Teacher, pk=pk)
    return render(request, 'lms_app/teacher_view.html', {'teachers': teachers} )


# @staff_member_required
class StudentList(ListView):
    queryset = Student.objects.all()
    context_object_name = 'students'
    template_name = 'lms_app/student_list.html'

# class StudentView(ListView):
#     queryset = Student.objects.all()
#     context_object_name = 'studentsV'
#     template_name = 'lms_app/student_view.html'
def StudentView(request, pk):
    students = get_object_or_404(Student, pk=pk)
    return render(request, 'lms_app/student_view.html', {'students': students} )

# def comments(request, pk):
#     msg = get_object_or_404(Video, pk=pk)
#     return render(request, 'lms_app/comment.html', {'msg': msg} )


def registepage(request):
    form = TeacherRegForm(request.POST or None, request.FILES or None)
    if form.is_valid():

        # handle_uploaded_file(request.FILES['file']) 
        form.cleaned_data
        form.save()
        return redirect('teacher_list')
    context = { 'form': form}
    return render(request, 'lms_app/register_teacher .html', context)


def studentpage(request):
    form = StudentRegister(request.POST , request.FILES )
    # register = Student.objects.all()
    if form.is_valid():
        form.cleaned_data
        print(form.cleaned_data)    
        form.save()
        return redirect('student_list') 
    context = {'form': form}
    return render(request, 'lms_app/register_student.html', context)

def load_syllabus(request):
    syllabus_id = request.GET.get('syllabus_id')
    stand = Standard.objects.filter(syllabus_id=syllabus_id).order_by('name')
    
    return render(request, 'lms_app/city_dropdown_list_options.html', {'stand': stand})

def load_scheme(request):
    standard_id = request.GET.get('standard_id')
    sch = Scheme.objects.filter(standard_id=standard_id).order_by('name')
    
    return render(request, 'lms_app/subject_dropdown.html', {'sch': sch})

def load_country(request):
    country_id = request.GET.get('country_id')
    city = Region.objects.filter(country_id=country_id).order_by('name')
    
    return render(request, 'lms_app/city_dropdown.html', {'city': city})


@staff_member_required
def video_list(request):
    chapter = request.GET.get('chapter')
    videos = Video.objects.all()
    if chapter is not None:
        videos = videos.filter(chapter__id__exact=chapter)
    context = {'videos': videos}
    return render(request, 'lms_app/videos_list.html', context)





    

def file_upload(request):
    form = VideoUpload(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.cleaned_data
        print(form.cleaned_data)
        upload_video = form.save(commit=False)
        student = Student.objects.filter(standard=upload_video.standard)
        print(student)
        devices = FCMDevice.objects.filter(user=student.user)
        devices.send_message("Video", upload_video.chapter)
        upload_video.save()
        return redirect('video')
    context = {'form': form}
    return render(request, 'lms_app/video_up.html', context)


class upload_document(ListView):
    queryset = Documents.objects.all()
    context_object_name = 'documents'
    template_name = 'lms_app/document_list.html'

def docs_upload(request):
    form = DocumentUpload(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.cleaned_data
        print(form.cleaned_data)
        form.save()
        return redirect('document')
    context = {'form': form}
    return render(request, 'lms_app/document_up.html', context)



# def load_cities(request):
#     country_id = request.GET.get('country_id')  
#     cities = City.objects.filter(country_id=country_id)
#     return render(request, 'lms_app/city_dropdown_list_options.html', {'cities': cities})


class Notification_list(ListView):
    queryset = Notification.objects.all()
    context_object_name = 'notification'
    template_name = 'lms_app/notification_list.html'

def notifi_up(request):
    form = NotificationAdd(request.POST or None, request.FILES or None)
    # register = Student.objects.all()
    if form.is_valid():
        form.cleaned_data
        print(form.cleaned_data)    
        form.save()
        return redirect('notify') 
    context = {'form': form}
    return render(request, 'lms_app/add_notification.html', context)


#class Profilep(ListView):
 #   queryset = Profile.objects.all()
  #  context_object_name = 'prof'
   # template_name = 'lms_app/profile_t.html'


class Upload_material(ListView):
    queryset = Study_Material.objects.all()
    context_object_name = 'study'
    template_name = 'lms_app/study_list.html'

def study_upload(request):
    form = StudyUpload(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.cleaned_data
        print(form.cleaned_data)
        form.save()
        return redirect('studyfile')
    context = {'form': form}
    return render(request, 'lms_app/study_up.html', context)


class Question_Paper(ListView):
    queryset = Question_paper.objects.all()
    context_object_name = 'question'
    template_name = 'lms_app/Question.html'

def question_upload(request):
    form = Question_form(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.cleaned_data
        print(form.cleaned_data)
        form.save()
        return redirect('questions')
    context = {'form': form}
    return render(request, 'lms_app/question_up.html', context)


def toggle(request):
    from django.apps import apps
    Model = apps.get_model("lms_app",request.POST['model'])
    w = Model.objects.get(id=request.POST['id'])
    w.active = not w.active
    w.save()
    

    return JsonResponse({"success": ""}, status=400)


def toggle_ispaid(request):
    from django.apps import apps
    Model = apps.get_model("lms_app",request.POST['model'])
    w = Model.objects.get(id=request.POST['id'])
    w.is_paid = not w.is_paid
    w.save()
    

    return JsonResponse({"success": ""}, status=400)

def commenting(request, pk):
    comment = request.POST.get('text', None)
    # if comment is None:
    #     context = {
    #         'error': "Comment is required"
    #     }
    #     return redirect(request, 'lms_app/videos_list.html',context)



    # video = Video.objects.get(pk=pk)
    video = get_object_or_404(Video, pk=pk)
    # video.comment.create(comment)
    Comment.objects.create(video=video, text=comment)
    # video.save()

    # form = Comments_Form(request.POST)
    # if form.is_valid():
    #     form.cleaned_data
    #     form.save()
    # return redirect('video')
    # context = {
    #     'form':form,
    #     'msg': msg
    # }

    return render(request,'lms_app/comment.html')
