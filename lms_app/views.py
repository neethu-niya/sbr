from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Syllabus, Standard, Subject, Chapter, Teacher, Student
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from lms_app.forms import SyllabusForm, StandardForm, SubjectForm, ChapterForm, TeacherRegForm, StudentRegister
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from .forms import *
# from lms_app.functions.functions import handle_uploaded_file

@staff_member_required
def syllabus_list(request):
    syllabus = Syllabus.objects.filter(active=True)
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
    standards = Standard.objects.filter(active=True)
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
    subjects = Subject.objects.filter(active=True)
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
    subject = request.GET.get('subject')
    chapters = Chapter.objects.filter(active=True)
    if subject is not None:
        chapters = chapters.filter(subject__id__exact=subject)
    form = ChapterForm(request.POST or None)
    if form.is_valid():
        form.cleaned_data
        form.save()
        return redirect('chapter_list')
    context = {'chapters': chapters, 'form': form}
    return render(request, 'lms_app/chapter_list.html', context)


class TeacherList(ListView):
    queryset = Teacher.objects.all()
    context_object_name = 'teachers'
    template_name = 'lms_app/teacher_list.html'

# @staff_member_required
class StudentList(ListView):
    queryset = Student.objects.all()
    context_object_name = 'students'
    template_name = 'lms_app/student_list.html'



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
    form = StudentRegister(request.POST or None, request.FILES or None)
    # register = Student.objects.all()
    if form.is_valid():
        form.cleaned_data
        print(form.cleaned_data)    
        form.save()
        return redirect('student_list')
    context = {'form': form}
    return render(request, 'lms_app/register_student.html', context)


class upload_video(ListView):
    queryset = Video.objects.all()
    context_object_name = 'videos'
    template_name = 'lms_app/videos_list.html'

def file_upload(request):
    form = VideoUpload(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.cleaned_data
        print(form.cleaned_data)
        form.save()
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

def load_cities(request):
    country_id = request.GET.get('country_id')  
    cities = City.objects.filter(country_id=country_id)
    return render(request, 'lms_app/city_dropdown_list_options.html', {'cities': cities})