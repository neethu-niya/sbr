# Generated by Django 3.0 on 2020-10-26 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0027_auto_20201026_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.ManyToManyField(blank=True, to='lms_app.Subject'),
        ),
    ]
