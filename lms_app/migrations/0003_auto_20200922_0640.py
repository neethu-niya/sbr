# Generated by Django 3.1.1 on 2020-09-22 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_auto_20200921_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='syllabus',
        ),
        migrations.AlterField(
            model_name='chat',
            name='uploaded_by',
            field=models.CharField(choices=[('0', 'Admin'), ('1', 'Teacher'), ('2', 'Student')], max_length=255),
        ),
        migrations.AlterField(
            model_name='file',
            name='uploaded_by',
            field=models.CharField(choices=[('0', 'Admin'), ('1', 'Teacher'), ('2', 'Student')], max_length=255),
        ),
    ]
