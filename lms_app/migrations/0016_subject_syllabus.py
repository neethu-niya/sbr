# Generated by Django 3.0 on 2020-09-24 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0015_student_syllabus'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='syllabus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms_app.Syllabus'),
        ),
    ]
