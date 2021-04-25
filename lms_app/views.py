from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import (
	Syllabus, Standard, Subject, Chapter, Teacher,
	Student, Documents, Study_Material, Question_paper
	)
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from lms_app.forms import (
	SyllabusForm, StandardForm, SubjectForm, ChapterForm,
	TeacherRegForm, StudentRegister, Comments_Form, ChapterVideoUpload
	)
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.http import HttpResponse
from django.http import JsonResponse
from fcm_django.models import FCMDevice
devices = FCMDevice.objects.all()
from django.contrib.auth.hashers import make_password

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

@staff_member_required
def syllabus_update(request, pk):
	syllabus = Syllabus.objects.get(id=pk)
	if request.method == 'POST':
		form = SyllabusForm(request.POST, request.FILES, instance=syllabus)
		if form.is_valid():
			form.save()
			return redirect('syllabus_list')
	else:
		form = SyllabusForm(instance=syllabus)
	context = {
	'form' : form,
	}
	return render(request, 'lms_app/syllabus_update.html', context)

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
def standard_update(request, pk):
	standard = Standard.objects.get(id=pk)
	if request.method == 'POST':
		form = StandardForm(request.POST, request.FILES, instance=standard)
		if form.is_valid():
			form.save()
			return redirect('standard_list')
	else:
		form = StandardForm(instance=standard)
	context = {
	'form' : form,
	}
	return render(request, 'lms_app/standard_update.html', context)

@staff_member_required
def subject_list(request):
	standard = request.GET.get('standard', None)
	subjects = Subject.objects.all()
	if standard is not None:
		subjects = subjects.filter(standard__id__exact=standard)
	form = SubjectForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.cleaned_data
		form.save()
		return redirect('subject_list')
	context = {'subjects': subjects, 'form': form}
	return render(request, 'lms_app/subject_list.html', context)


@staff_member_required
def subject_update(request, pk):
	subject = Subject.objects.get(id=pk)
	if request.method == 'POST':
		form = SubjectForm(request.POST, request.FILES, instance=subject)
		if form.is_valid():
			form.save()
			return redirect('subject_list')
	else:
		form = SubjectForm(instance=subject)
	context = {
	'form' : form,
	}
	return render(request, 'lms_app/subject_update.html', context)

@staff_member_required
def chapter_list(request):
	subject = request.GET.get('subject', None)
	chapters = Chapter.objects.all()
	if subject is not None:
		chapters = chapters.filter(subject__id__exact=subject)
	form = ChapterForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.cleaned_data
		form.save()
		return redirect('chapter_list')
	context = {'chapters': chapters, 'form': form}
	return render(request, 'lms_app/chapter_list.html', context)


@staff_member_required
def chapter_update(request, pk):
	chapter = Chapter.objects.get(id=pk)
	if request.method == 'POST':
		form = ChapterForm(request.POST, request.FILES, instance=chapter)
		if form.is_valid():
			form.save()
			return redirect('chapter_list')
	else:
		form = ChapterForm(instance=chapter)
	context = {
	'form' : form,
	}
	return render(request, 'lms_app/chapter_update.html', context)



@staff_member_required
def scheme_list(request):
	subject = request.GET.get('subject')
	schemes = Scheme.objects.all()
	# if subject is not None:
	#     schemes = schemes.filter(subject__id__exact=subject)
	# form = SchemeForm(request.POST or None)
	# if form.is_valid():
	#     print(form.cleaned_data)
	#     form.cleaned_data
	#     form.save()
	#     return redirect('scheme_list')
	context = {'schemes': schemes}
	return render(request, 'lms_app/scheme_list.html', context)

@staff_member_required
def scheme_upload(request):
	form = SchemeForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('scheme_list')
	context = {'form': form}
	return render(request, 'lms_app/scheme_upload.html', context)

@staff_member_required
def scheme_update(request, pk):
	scheme = Scheme.objects.get(id=pk)
	if request.method == 'POST':
		form = SchemeForm(request.POST, request.FILES, instance=scheme)
		if form.is_valid():
			form.save()
			return redirect('scheme_list')
	else:
		form = SchemeForm(instance=scheme)
	context = {
	'form' : form,
	}
	return render(request, 'lms_app/scheme_update.html', context)




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

@staff_member_required
def registepage(request):
	form = TeacherRegForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		teacher = form.save(commit=False)
		teacher.password = make_password(form.cleaned_data["password"])
		teacher.save()
		return redirect('teacher_list')
	context = { 'form': form}
	return render(request, 'lms_app/register_teacher.html', context)

@staff_member_required
def teacher_update(request, pk):
	teacher = Teacher.objects.get(id=pk)
	if request.method == 'POST':
		form = TeacherRegForm(request.POST, request.FILES, instance=teacher)
		if form.is_valid():
			teacher = form.save(commit=False)
			teacher.password = make_password(form.cleaned_data["password"])
			teacher.save()
			return redirect('teacher_list')
	else:
		form = TeacherRegForm(instance=teacher)
	context = {
	'form' : form,
	}
	return render(request, 'lms_app/teacher_update.html', context)


def studentpage(request):
	form = StudentRegister(request.POST , request.FILES )
	# register = Student.objects.all()
	if form.is_valid():
		student = form.save(commit=False)
		student.password = make_password(form.cleaned_data["password"])
		student.save()
		return redirect('student_list') 
	context = {'form': form}
	return render(request, 'lms_app/register_student.html', context)

@staff_member_required
def student_update(request, pk):
	student = Student.objects.get(id=pk)
	if request.method == 'POST':
		form = StudentRegister(request.POST, request.FILES, instance=student)
		if form.is_valid():
			student = form.save(commit=False)
			student.password = make_password(form.cleaned_data["password"])
			student.save()
			return redirect('student_list')
	else:
		form = StudentRegister(instance=student)
	context = {
	'form' : form,
	}
	return render(request, 'lms_app/student_update.html', context)

def load_standard(request):
	syllabus_id = request.GET.get('syllabus_id')
	stand = Standard.objects.filter(syllabus_id=syllabus_id, active=True).order_by('name')
	
	return render(request, 'lms_app/city_dropdown_list_options.html', {'stand': stand})

def load_subject(request):
	standard_id = request.GET.get('standard_id')
	subj = Subject.objects.filter(standard_id=standard_id, active=True).order_by('name')
	
	return render(request, 'lms_app/subject_dropdown.html', {'subj': subj})

def load_chapter(request):
	subject_id = request.GET.get('subject_id')
	cha = Chapter.objects.filter(subject_id=subject_id, active=True).order_by('name')
	
	return render(request, 'lms_app/chapter_dropdown.html', {'cha': cha})




def load_scheme(request):
	standard_id = request.GET.get('standard_id')
	sch = Scheme.objects.filter(standard_id=standard_id).order_by('name')
	
	return render(request, 'lms_app/scheme_dropdown.html', {'sch': sch})

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
		upload_video = form.save(commit=False)
		standard = upload_video.standard
		users = User.objects.filter(student__standard=standard)
		for user in users:
			FCMDevice.objects.filter(user=user).send_message(title="Uploaded New Video", body=f"{upload_video.name} in chapter {upload_video.chapter}.")
		upload_video.save()
		return redirect('video')
	else:
		form = VideoUpload()
	context = {'form': form}
	return render(request, 'lms_app/video_up.html', context)


def video_update(request, pk): 
	video = Video.objects.get(id=pk)
	if request.method == 'POST':
		form = VideoUpload(request.POST, request.FILES or None, instance=video)
		if form.is_valid():
			form.save()
			return redirect('video')
	else:
		form = VideoUpload(instance=video)
	context = {
	'form' : form,
	}
	return render(request, 'lms_app/video_up.html', context)


class upload_document(ListView):
	queryset = Documents.objects.all()
	context_object_name = 'documents'
	template_name = 'lms_app/document_list.html'

def docs_upload(request):
	form = DocumentUpload(request.POST or None , request.FILES or None)
	if form.is_valid():
		upload_doc = form.save(commit=False)
		standard = upload_doc.standard
		users = User.objects.filter(student__standard=standard)
		for user in users:
			FCMDevice.objects.filter(user=user).send_message(title="Uploaded New Document", body=f"{upload_doc.name} in chapter {upload_doc.chapter}.")
		upload_doc.save()
		return redirect('document')
	context = {'form': form}
	return render(request, 'lms_app/document_up.html', context)


def docs_update(request, pk): 
	documents = Documents.objects.get(id=pk)
	if request.method == 'POST':
		form = DocumentUpload(request.POST, request.FILES or None, instance=documents)
		if form.is_valid():
			form.save()
			return redirect('document')
	else:
		form = DocumentUpload(instance=documents)
	context = {
	'form' : form,
	}
	return render(request, 'lms_app/document_up.html', context)



# def load_cities(request):
#     country_id = request.GET.get('country_id')  
#     cities = City.objects.filter(country_id=country_id)
#     return render(request, 'lms_app/city_dropdown_list_options.html', {'cities': cities})


class Notification_list(ListView):
	queryset = Notification.objects.all()
	context_object_name = 'notification'
	template_name = 'lms_app/notification_list.html'

@staff_member_required
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

@staff_member_required
def notification_update(request, pk):
	notification = Notification.objects.get(id=pk)
	if request.method == 'POST':
		form = NotificationAdd(request.POST, request.FILES, instance=notification)
		if form.is_valid():
			form.save()
			return redirect('notify')
	else:
		form = NotificationAdd(instance=notification)
	context = {
	'form' : form,
	}
	return render(request, 'lms_app/notification_update.html', context)


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
		upload_study = form.save(commit=False)
		standard = upload_study.standard
		users = User.objects.filter(student__standard=standard)
		for user in users:
			FCMDevice.objects.filter(user=user).send_message(title="Uploaded New Study Material", body=f"{upload_study.name} in chapter {upload_study.chapter}.")
		upload_study.save()
		return redirect('studyfile')
	context = {'form': form}
	return render(request, 'lms_app/study_up.html', context)

@staff_member_required
def study_update(request, pk):
	study_material = Study_Material.objects.get(id=pk)
	if request.method == 'POST':
		form = StudyUpload(request.POST, request.FILES, instance=study_material)
		if form.is_valid():
			form.save()
			return redirect('studyfile')
	else:
		form = StudyUpload(instance=study_material)
	context = {
	'form' : form,
	}
	return render(request, 'lms_app/study_material_update.html', context)



class Question_Paper(ListView):
	queryset = Question_paper.objects.all()
	context_object_name = 'question'
	template_name = 'lms_app/Question.html'

def question_upload(request):
	form = Question_form(request.POST or None , request.FILES or None)
	if form.is_valid():
		upload_quest = form.save(commit=False)
		standard = upload_quest.standard
		users = User.objects.filter(student__standard=standard)
		for user in users:
			FCMDevice.objects.filter(user=user).send_message(title="Uploaded New Question Paper", body=f"{upload_quest.name} in chapter {upload_quest.chapter}.")
		upload_quest.save()
		return redirect('questions')
	context = {'form': form}
	return render(request, 'lms_app/question_up.html', context)

def question_update(request, pk): 
	question = Question_paper.objects.get(id=pk)
	if request.method == 'POST':
		form = Question_form(request.POST, request.FILES or None, instance=question)
		if form.is_valid():
			form.save()
			return redirect('questions')
	else:
		form = Question_form(instance=question)
	context = {
	'form' : form,
	}
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

def toggle_freetier(request):
	from django.apps import apps
	Model = apps.get_model("lms_app",request.POST['model'])
	w = Model.objects.get(id=request.POST['id'])
	w.free_tier = not w.free_tier
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


def chapter_video_upload(request, pk):
	chapter = Chapter.objects.get(id=pk)
	if request.method == 'POST':
		form = ChapterVideoUpload(request.POST, request.FILES)
		if form.is_valid():
			video = form.save(commit=False)
			video.syllabus = chapter.syllabus
			video.standard = chapter.standard
			video.subject = chapter.subject
			video.chapter = chapter
			video.save()
			return redirect('lms_app/videos_list.html')
	else:
		form = ChapterVideoUpload()
	context = {
	'form' : form,
	}
	return render(request, 'lms_app/video_up.html', context)