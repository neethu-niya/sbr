# Generated by Django 3.0 on 2020-09-24 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0016_subject_syllabus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='syllabus',
        ),
    ]
