from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from cities_light.models import City, Country, Region


# from lms_app.forms import RegisterForm
User = get_user_model()


login_choices = [
    ('0', 'Web'),
    ('1', 'App'),
]

ROLES = [
    ('0', 'Admin'),
    ('1', 'Teacher'),
    ('2', 'Student'),
]


material_choices = [
    ('0', 'Study Material'),
    ('1', 'Questionnaire'),
    ('2', 'Previous year Question'),
]

file_choices = [
    ('0', 'Video'),
    ('1', 'Image'),
    ('2', 'pdf'),
]


send_choices = [
    ('Teacher', 'Teachers'),
    ('Student', 'Students'),
]

scheme_choices = [
    ('0', 'Subject'),
    ('1', 'Chapter'),
]

state_choices = [
    ('KL', 'KERALA'),
    ('KA', 'KARNATAKA'),
    ('TN', 'TAMIL NADU'),
    ('GOA', 'GOA'),
]

class Syllabus(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Syllabus'
        verbose_name_plural = 'Syllabus'

    def __str__(self):
        return self.name


class Standard(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False, null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return str(self.syllabus)
        return f"{self.syllabus} - {self.name}"
    
    def get_absolute_url(self):
        return reverse("standard_list", kwargs={"pk": self.pk})
    



class Subject(models.Model):
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        # return f"{self.standard} - {self.name}"

    @property
    def get_standard(self):
        return self.standard.name
    

    # @property
    # def subjects(self):
    #     subs =  self.subject.all()
    #     _subs = []
    #     for sub in subs:
    #         _subs.append(str(sub))
    #     from django.utils.html import format_html
    #     return format_html(", ".join(_subs)) 


class Teacher(models.Model):
    # boolChoice = (
    #     ("M","Male"),("F","Female")
    #     )
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    contact_no_1 = PhoneNumberField(
        default=None, null=True, blank=True, unique=True)
    whatsapp_no = PhoneNumberField(
        default=None, null=True, blank=True, unique=True)
    address = models.CharField(max_length=255)
    subject = models.ManyToManyField(Subject, blank=True)
    material_type = models.CharField(max_length=50, choices=file_choices,  null=True,  blank=True)

    image = models.ImageField(
        upload_to='staticfiles/image/',null=True, blank=True)
   
    #hanin created gender
    # gender = models.CharField(max_length = 6,choices=boolChoice, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  null=True, blank=True, on_delete=models.CASCADE)
    
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        u = User.objects.create(username=self.name,password = "helloworld555")
        # self.user.username = self.name
        # self.user.password = "helloworld555"
        self.user=u
        super(Teacher, self).save(self, *args, **kwargs)





    @receiver(post_save, sender=User)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
# 

class Chapter(models.Model):
    subject = models.ManyToManyField(Subject)
    #foreignkey
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    

    class Meta:
        verbose_name = 'Chapter'
        verbose_name_plural = 'Chapters'


    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    # description = models.TextField()
    description = models.TextField()
    subject = models.ManyToManyField(Subject, blank=True)


    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    videofile = models.FileField(
        upload_to='staticfiles/media_root/videos/', null=True)
    image = models.ImageField(
        upload_to='staticfiles/image/', null=True, blank=True)
    thumbnail_image = models.ImageField(
        upload_to='staticfiles/thumbnail/', null=True, blank=True)
    url_field = models.URLField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name  + ": " + str(self.videofile)
        # + ": " + str(self.videofile)





class Chat(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='staticfiles/image/', null=True, blank=True)
    pdf = models.FileField(upload_to='staticfiles/pdf')
    remark = models.CharField(max_length=200)
    uploaded_by = models.CharField(max_length=255, choices=ROLES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




class Scheme(models.Model):
    scheme_name = models.CharField(max_length=255, null=True, blank=True)
     
    subject_wise = models.ManyToManyField(Subject)

    # subs =  self.subject.all()
    # _subs = []
    # for sub in subs:
    #     _subs.append(str(sub))
    #     from django.utils.html import format_html
    # return format_html(", ".join(_subs))

    # def __str__(self):
    #     subject = self.subject_wise.all()
    #     for sub in subject:
    #         sub
    # return str(sub)




# class UserProfile(models.Model):
#     country = models.ForeignKey(Country ,on_delete=models.CASCADE)
#     state = models.ForeignKey(Region ,on_delete=models.CASCADE)
#   
# class Countrys(models.Model):
#     country = models.ForeignKey(Country,on_delete=models.CASCADE)
#     active = models.BooleanField(default=False)
    

#     def __str__(self):
#         return f'{self.country}' 
    
#         # return f'{self.country}'    


# class State(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     name = models.ForeignKey(Region, on_delete=models.CASCADE, null=True,  blank=True)
    

#     def __str__(self):
#         return f'{self.name}' 



class Student(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # gender = models.CharField(max_length=6, choices=gender_choices)
    # date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    country = models.ForeignKey(Country ,on_delete=models.CASCADE,null=True)

    state = models.ForeignKey(Region ,on_delete=models.CASCADE,null=True)
    city = models.CharField(null=True,blank=True,max_length=255)

    # country = CountryField(blank_label='(select country)',null=True, blank=True)
    # state = models.ForeignKey(State, on_delete=models.CASCADE)
    

    # nationality = models.CharField(null=True,blank=True,max_length=255)
    # state = models.CharField(null=True,blank=True,max_length=255)
    district = models.CharField(null=True,blank=True,max_length=255)
    present_country = models.ForeignKey(Country ,on_delete=models.CASCADE,null=True,related_name = 'pre_country')
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(
        upload_to='staticfiles/image/', null=True, blank=True)
    guardian_name = models.CharField(null=True,blank=True,max_length=255)
    guardian_relation = models.CharField(null=True,blank=True,max_length=50)
    contact_no = PhoneNumberField(
        default=None, null=True, blank=True, unique=True)
    whatsapp_no = PhoneNumberField(
        default=None, null=True, blank=True, unique=True)
    syllabus = models.ForeignKey(Syllabus,null=True,blank=True, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    # HANIN ADDED SUBJECT FIELD
    subject = models.ManyToManyField(Subject, blank=True)
    # scheme = models.ForeignKey(Scheme,null=True,blank=True, on_delete=models.CASCADE)
    course_type = models.CharField(null=True,blank=True,max_length=255)
    user = models.ForeignKey(get_user_model(),  null=True, blank=True, on_delete=models.CASCADE)
    
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name)
        if not user:

            s = User.objects.create(username=self.name,password = make_password("worldheloo666"))
            # self.user.username = self.name
            # self.user.password = "helloworld555"
            self.user=s
        
        else:
            pass
        super(Student, self).save(self, *args, **kwargs)

    

    
        
# @receiver(post_save, sender=Student)
# def create_or_update_studentuser(sender, instance, created, **kwargs):
#     if created:
#         User.objects.create(username=instance.name,password=str(instance.contact_no),
#                             email=instance.email,user_type="2")

class Documents(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255 )
    description = models.TextField(null=True, blank=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    # material_type = models.CharField(max_length=50, choices=material_choices,  null=True,  blank=True)
    url_field = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(
        upload_to='staticfiles/image/', null=True, blank=True)
    thumbnail_image = models.ImageField(
        upload_to='staticfiles/thumbnail/', null=True, blank=True)
    pdf = models.FileField(upload_to='staticfiles/pdf')
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'


    def __str__(self):
        return self.name

class Study_Material(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255 )
    description = models.TextField(null=True, blank=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    # material_type = models.CharField(max_length=50, choices=material_choices,  null=True,  blank=True)
    url_field = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(
        upload_to='staticfiles/image/', null=True, blank=True)
    thumbnail_image = models.ImageField(
        upload_to='staticfiles/thumbnail/', null=True, blank=True)
    pdf = models.FileField(upload_to='staticfiles/pdf')
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Study_Material'
        verbose_name_plural = 'Study_Materials'


    def __str__(self):
        return self.name

class Question_paper(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255 )
    description = models.TextField(null=True, blank=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    # material_type = models.CharField(max_length=50, choices=material_choices,  null=True,  blank=True)
    url_field = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(
        upload_to='staticfiles/image/', null=True, blank=True)
    thumbnail_image = models.ImageField(
        upload_to='staticfiles/thumbnail/', null=True, blank=True)
    pdf = models.FileField(upload_to='staticfiles/pdf')
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Question_paper'
        verbose_name_plural = 'Question_papers'


    def __str__(self):
        return self.name


class File(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='staticfiles/image/', null=True, blank=True)
    pdf = models.FileField(upload_to='staticfiles/pdf')
    remark = models.CharField(max_length=200)
    uploaded_by = models.CharField(max_length=255, choices=ROLES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Notification(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='staticfiles/image/', null=True, blank=True)
    description = models.TextField()
    send_to = models.CharField(max_length=255, choices=send_choices)

    def __str__(self):
        return self.title       


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(
#         upload_to='staticfiles/image/', null=True, blank=True)
        
#     def __str__(self):
#         return f'{self.user.name} Profile'
     
    # def save(self, *args, **kwargs):
    #     s = User.objects.get()
    #     # self.user.username = self.name
    #     # self.user.password = "helloworld555"
    #     self.user=s
    #     super(Student, self).save(self, *args, **kwargs)
