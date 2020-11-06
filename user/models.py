from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

# from lms_app.models import 

ROLES = [
    ('0', 'Admin'),
    ('1', 'Teacher'),
    ('2', 'Student'),
]

login_choices = [
    ('0', 'Web'),
    ('1', 'App'),
]


class User(AbstractUser):
    user_type = models.CharField(null=True, blank=True,max_length=50, choices=ROLES)
    phone = PhoneNumberField(default=None, null=True, blank=True, unique=True)
    email = models.EmailField(null=True, blank=True)
    last_login_time = timezone.now()
    
    device_id = models.CharField(max_length=255, null=True, blank=True,)
    firebase_token = models.CharField(max_length=255, null=True, blank=True,)
    login_from = models.CharField(max_length=10, choices=login_choices, null=True, blank=True,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
# hanin added @reciever
# @receiver(post_save, sender=Teacher)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         User.objects.create(teacher=instance)
#         instance.user.save()

# @receiver(post_save, sender=Teacher)
# def create_or_update_user_profile   (sender, instance, created, **kwargs):
    
#     if created:
#         u = User.objects.get(username=instance.name)
#         Teacher.objects.update(user=u)