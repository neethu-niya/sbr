# Generated by Django 3.0 on 2020-12-29 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_auto_20201211_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='standard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms_app.Standard'),
        ),
        migrations.AddField(
            model_name='documents',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms_app.Subject'),
        ),
        migrations.AddField(
            model_name='documents',
            name='syllabus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms_app.Syllabus'),
        ),
        migrations.AddField(
            model_name='video',
            name='standard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms_app.Standard'),
        ),
        migrations.AddField(
            model_name='video',
            name='syllabus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms_app.Syllabus'),
        ),
    ]
