# Generated by Django 3.0 on 2020-09-24 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0018_auto_20200924_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='chapter_wise',
        ),
        migrations.AddField(
            model_name='scheme',
            name='scheme_choice',
            field=models.CharField(choices=[('0', 'Subject'), ('1', 'Chapter')], default=1, max_length=255),
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='subject_wise',
        ),
        migrations.AddField(
            model_name='scheme',
            name='subject_wise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms_app.Subject'),
        ),
    ]
