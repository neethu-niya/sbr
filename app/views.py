# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from lms_app.models import Student, Teacher, User, Syllabus, Standard

@login_required(login_url="/login/")
def index(request):
    count = Student.objects.all().count()
    count_teacher = Teacher.objects.all().count()
    Total_user = User.objects.exclude(is_superuser=1).count()
    syllabus_count = Syllabus.objects.all().count()
    standard_count = Standard.objects.filter(syllabus_id=1).count()
    syllabus_all  = Syllabus.objects.get(id=1)
    syllabus_name = syllabus_all.name
    context = {
        'students_count': count,
        'teacher_count' : count_teacher,
        'user_count'    : Total_user,
        'syllabus_c': syllabus_count,
        'standard_c': standard_count,
        'syllabus_txt': syllabus_all,
        'syllabus_n'  : syllabus_name
    }

    return render(request, "index.html", context)

def index2(request):
    return render(request, "index2.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
