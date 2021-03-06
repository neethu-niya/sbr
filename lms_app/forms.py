from django import forms
from .models import Syllabus, Standard, Subject, Chapter, Teacher, Student, Scheme,  Video, Documents, Notification, Question_paper, Study_Material, Comment
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from cities_light.models import City, Country, Region
from django_select2.forms import ModelSelect2Widget     

material_choices = [
    ('0', 'Study Material'),
    ('1', 'Questionnaire'),
    ('2', 'Previous year Question'),
]

send_choices = [
    ('Teacher', 'Teachers'),
    ('Student', 'Students'),
]

# state_choices = [
#     ('KL', 'KERALA'),
#     ('KA', 'KARNATAKA'),
#     ('TN', 'TAMIL NADU'),

class SyllabusForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", id: "addName", 'placeholder' :"enter syllabus name"}))
    active = forms.BooleanField(required=False)

    class Meta:
        model = Syllabus
        fields = ['name', 'active']


class StandardForm(forms.ModelForm):
    syllabus = forms.ModelChoiceField(queryset=Syllabus.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", id: "addName", 'placeholder' :"enter standard name"}))
    active = forms.BooleanField(required=False)

    class Meta:
        model = Standard
        fields = ['syllabus', 'name', 'active']



class SubjectForm(forms.ModelForm):
    syllabus = forms.ModelChoiceField(queryset=Syllabus.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    standard = forms.ModelChoiceField(queryset=Standard.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", id: "addName", 'placeholder' :"enter subject name"}))
    image   = forms.ImageField()
    active = forms.BooleanField(required=False)

    class Meta:
        model = Subject
        fields = ['syllabus', 'standard', 'name', 'image', 'active']


class ChapterForm(forms.ModelForm):
    syllabus = forms.ModelChoiceField(queryset=Syllabus.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    standard = forms.ModelChoiceField(queryset=Standard.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), widget=forms.Select(attrs={"class":"form-control", type: "select", id:"addPosition"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", id: "addName", 'placeholder' :"enter subject name"}))
    image   = forms.ImageField()
    active = forms.BooleanField(required=False)
    free_tier = forms.BooleanField(required=False)

    class Meta:
        model = Chapter
        fields = ['syllabus', 'standard', 'subject', 'name', 'image', 'free_tier', 'active']





class SchemeForm(forms.ModelForm):

    class Meta:
        model = Scheme
        fields = ['syllabus', 'standard', 'subject', 'name']
   

class TeacherRegForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=False, help_text='Optional.')  
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    contact_no_1 = forms.CharField(max_length=30, required=False)
    whatsapp_no = forms.CharField(max_length=30, required=False)
    address = forms.CharField(max_length=50, required=False)
    subject = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.SelectMultiple(attrs={"class":"form-control", id:"exampleFormControlSelect2"}))
    image   = forms.ImageField()
    password = forms.CharField(min_length=6, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    # gender = forms.CharField(max_length=30, required=False, help_text='Optional.')  
    
    active = forms.BooleanField(required=False)
    class Meta:
        model = Teacher
        fields = ('name', 'email', 'username', 'password', 'contact_no_1', 'whatsapp_no', 'address', 'subject', 'image',
                  'active')



class StudentRegister(forms.ModelForm):
    syllabus = forms.ModelChoiceField(queryset=Syllabus.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    standard = forms.ModelChoiceField(queryset=Standard.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    present_country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    state = forms.ModelChoiceField(queryset=Region.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    scheme = forms.ModelChoiceField(queryset=Scheme.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    password = forms.CharField(min_length=6, widget=forms.TextInput(attrs={'class' : 'form-control'}))


    class Meta:
        model = Student
        fields = ('name', 'username', 'password', 'address','country','state','city','district','present_country','email',
                  'course_type','image','guardian_name', 'guardian_relation', 'contact_no', 'whatsapp_no',
                  'syllabus','standard', 'scheme',  'is_paid', 'course_type','active')
    # class Meta:
    #     model = Student
    #     fields = '__all__'


    


class VideoUpload(forms.ModelForm):
    videofile = forms.FileField(required=False)

    class Meta:
        model = Video
        fields = ('name', 'subtitle', 'description', 'syllabus', 'standard','subject', 'chapter',   'image', 
                 'thumbnail_image', 'vimeo_video', 'videofile')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['standard'].queryset = Standard.objects.none()


    #     if 'syllabus' in self.data:
    #         try:    
    #             syllabus_id = int(self.data.get('syllabus'))
    #             self.fields['standard'].queryset = Standard.objects.filter(id=syllabus_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['standard'].queryset = self.instance.syllabus.standard_set.order_by('name')


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['subject'].queryset = Subject.objects.none()


    #     if 'standard' in self.data:
    #         try:    
    #             standard_id = int(self.data.get('standard'))
    #             self.fields['subject'].queryset = Subject.objects.filter(id=standard_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['subject'].queryset = self.instance.standard.subject_set.order_by('name')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['chapter'].queryset = Chapter.objects.none()


    #     if 'subject' in self.data:
    #         try:    
    #             subject_id = int(self.data.get('subject'))
    #             self.fields['chapter'].queryset = Chapter.objects.filter(id=subject_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['chapter'].queryset = self.instance.subject.chapter_set.order_by('name')
 
    



class DocumentUpload(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ('name','subtitle', 'description','syllabus', 'standard','subject', 'chapter',  'image', 
                  'thumbnail_image', 'pdf')

    

    

class StudyUpload(forms.ModelForm):
    class Meta:
        model = Study_Material
        fields = ('name','subtitle', 'description', 'syllabus', 'standard','subject', 'chapter', 'image', 
                  'thumbnail_image', 'pdf')


    
# class Comment_form(forms.ModelForm):
#     Video = forms.ModelChoiceField(queryset=Comment.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"})))



class Question_form(forms.ModelForm):
    class Meta:
        model = Question_paper
        fields = ('name','subtitle', 'description', 'syllabus', 'standard','subject', 'chapter', 'image', 
                  'thumbnail_image', 'pdf')
    

   


class NotificationAdd(forms.ModelForm):
    title = forms.CharField(max_length=255, required=False)
    image = forms.ImageField()
    description = forms.Textarea()
    send_to = forms.ChoiceField(choices=send_choices, required=False)
    class Meta:
        model = Notification
        fields = ('title','image', 'description', 'send_to')


class Comments_Form(forms.ModelForm):
    video = forms.ModelChoiceField(queryset=Video.objects.all(), required=False, widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    text =  forms.Textarea()
    class Meta:
        model = Comment
        fields = ('video','text')


class ChapterVideoUpload(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('name', 'subtitle', 'description', 'image', 
                 'thumbnail_image', 'videofile')