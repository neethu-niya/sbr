# Generated by Django 3.0 on 2020-11-04 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0043_auto_20201104_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.AddField(
            model_name='country',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lms_app.City'),
        ),
    ]
