from django import forms
from .models import Syllabus, Standard, Subject, Chapter, Teacher, Student, Scheme,  Video, Documents, Notification, Question_paper, Study_Material, Comment
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from cities_light.models import City, Country, Region

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
    standard = forms.ModelChoiceField(queryset=Standard.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", id: "addName", 'placeholder' :"enter subject name"}))
    active = forms.BooleanField(required=False)

    class Meta:
        model = Subject
        fields = ['standard', 'name', 'active']


class ChapterForm(forms.ModelForm):
    subject = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.SelectMultiple(attrs={"class":"form-control", id:"exampleFormControlSelect2"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", id: "addName", 'placeholder' :"enter subject name"}))
    active = forms.BooleanField(required=False)

    class Meta:
        model = Chapter
        fields = ['subject', 'name', 'active']





class SchemeForm(forms.ModelForm):
    subject= forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.SelectMultiple(attrs={"class":"form-control", id:"exampleFormControlSelect2"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", id: "addName", 'placeholder' :"enter Scheme name"}))
    active = forms.BooleanField(required=False)

    class Meta:
        model = Scheme
        fields = ['subject', 'name', 'active']

class TeacherRegForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=False, help_text='Optional.')  
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    contact_no_1 = forms.CharField(max_length=30, required=False)
    whatsapp_no = forms.CharField(max_length=30, required=False)
    address = forms.CharField(max_length=50, required=False)
    subject = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.SelectMultiple(attrs={"class":"form-control", id:"exampleFormControlSelect2"}))
    image   = forms.ImageField()
    # gender = forms.CharField(max_length=30, required=False, help_text='Optional.')  
    
    active = forms.BooleanField(required=False)
    class Meta:
        model = Teacher
        fields = ('name', 'email',  'contact_no_1', 'whatsapp_no', 'address', 'subject', 'image',
                  'active')



class StudentRegister(forms.ModelForm):
    # name = forms.CharField(max_length=30, required=False, help_text='Optional')  
    # address = forms.CharField(max_length=50, required=False)
   
    # country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    # state = forms.ModelChoiceField(queryset=Region.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    # city = forms.CharField(max_length=255, required=False)
    
    
    # # state = forms.CharField(max_length=255)
    # district = forms.CharField(max_length=255,required=False)
    # present_country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # subject = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.SelectMultiple(attrs={"class":"form-control", id:"exampleFormControlSelect2"}))
    # image = forms.ImageField()
    # guardian_name = forms.CharField(max_length=255)
    # guardian_relation = forms.CharField(max_length=50)
    # contact_no = forms.CharField(max_length=30, required=False)
    # whatsapp_no = forms.CharField(max_length=30, required=False)
    # # gender = forms.CharField(max_length=6, required=False)
    # standard = forms.ModelChoiceField(queryset=Standard.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    
    # syllabus = forms.ModelChoiceField(queryset=Syllabus.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    # # Syllabus = forms.ModelMultipleChoiceField(queryset=Syllabus.objects.all(), widget=forms.SelectMultiple(attrs={"class":"form-control", id:"exampleFormControlSelect2"}))
    # subject = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.SelectMultiple(attrs={"class":"form-control", id:"exampleFormControlSelect2"}))
    # # scheme = forms.ModelChoiceField(queryset=Scheme.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    # course_type = forms.CharField(max_length=255)
    # active = forms.BooleanField(required=False)

    #want to work on user unique
    #user = User.objects.get(username=self.name)

    class Meta:
        model = Student
        fields = ('name', 'address','country','state','city','district','present_country','email',
                  'course_type','image','guardian_name', 'guardian_relation', 'contact_no', 'whatsapp_no',
                  'syllabus','standard','course_type','active')
    # class Meta:
    #     model = Student
    #     fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['standard'].queryset = Standard.objects.none()


        if 'syllabus' in self.data:
            try:
                syllabus_id = int(self.data.get('syllabus'))
                self.fields['standard'].queryset = Standard.objects.filter(id=syllabus_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk and self.instance.standard is not None:
            self.fields['standard'].queryset = self.instance.syllabus.standard_set.order_by('name')
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.none()


        if 'standard' in self.data:
            try:    
                standard_id = int(self.data.get('standard'))
                self.fields['subject'].queryset = Subject.objects.filter(id=standard_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['subject'].queryset = self.instance.standard.subject_set.order_by('name')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = Region.objects.none()


        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = Region.objects.filter(id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk and self.instance.standard is not None:
            self.fields['state'].queryset = self.instance.country.state_set.order_by('name')


class VideoUpload(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    subtitle = forms.CharField(max_length=255, required=False)
    description =forms.Textarea()
    subject = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.SelectMultiple(attrs={"class":"form-control", id:"exampleFormControlSelect2"}))
    chapter = forms.ModelChoiceField(queryset=Chapter.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))
    
    # chapter =forms.ModelChoiceField(Chapter, on_delete=models.CASCADE)
    # upload_to='staticfiles/media_root/videos/'
    # upload_to='staticfiles/image/'
    # upload_to='staticfiles/thumbnail/',
    videofile =forms.FileField()
    image =forms.ImageField()
    thumbnail_image =forms.ImageField()
    url_field =forms.URLField(max_length=200, required=False)
    active =forms.BooleanField(required=False)
    class Meta:
       model = Video
       fields = ('name', 'subtitle', 'description', 'subject', 'chapter',  'videofile', 'image', 
                 'thumbnail_image','url_field', 'active')

# class VideoUpload(forms.ModelForm):
#     class Meta:
#         model = 'videos'
#         fields = '__all__'

class DocumentUpload(forms.ModelForm):
    name = forms.CharField(max_length=255, required=False)
    subtitle = forms.CharField(max_length=255, required=False)
    description = forms.Textarea()
    chapter = forms.ModelChoiceField(queryset=Chapter.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))

    # material_type = forms.ChoiceField(choices = material_choices)

    image = forms.ImageField(required=False)
    thumbnail_image = forms.ImageField(required=False)
        
    pdf = forms.FileField(required=False)
    url_field =forms.URLField(max_length=200, required=False)

    active = forms.BooleanField(required=False)
    class Meta:
        model = Documents
        fields = ('name','subtitle', 'description', 'chapter',  'image', 
                  'thumbnail_image', 'pdf','url_field', 'active')

class StudyUpload(forms.ModelForm):
    name = forms.CharField(max_length=255, required=False)
    subtitle = forms.CharField(max_length=255, required=False)
    description = forms.Textarea()
    chapter = forms.ModelChoiceField(queryset=Chapter.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))

    # material_type = forms.ChoiceField(choices = material_choices)

    image = forms.ImageField(required=False)
    thumbnail_image = forms.ImageField(required=False)
        
    pdf = forms.FileField(required=False)
    url_field =forms.URLField(max_length=200, required=False)
# Study_Material
    active = forms.BooleanField(required=False)
    class Meta:
        model = Study_Material
        fields = ('name','subtitle', 'description', 'chapter', 'image', 
                  'thumbnail_image', 'pdf','url_field', 'active')


# class Comment_form(forms.ModelForm):
#     Video = forms.ModelChoiceField(queryset=Comment.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"})))



class Question_form(forms.ModelForm):
    name = forms.CharField(max_length=255, required=False)
    subtitle = forms.CharField(max_length=255, required=False)
    description = forms.Textarea()
    chapter = forms.ModelChoiceField(queryset=Chapter.objects.all(), widget=forms.Select(attrs={"class":"form-control",type: "select", id:"addPosition"}))

    # material_type = forms.ChoiceField(choices = material_choices)

    image = forms.ImageField(required=False)
    thumbnail_image = forms.ImageField(required=False)
        
    pdf = forms.FileField(required=False)
    url_field =forms.URLField(max_length=200, required=False)

    active = forms.BooleanField(required=False)
    class Meta:
        model = Question_paper
        fields = ('name','subtitle', 'description', 'chapter', 'image', 
                  'thumbnail_image', 'pdf','url_field', 'active')


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
