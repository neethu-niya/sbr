# Generated by Django 3.0 on 2020-10-26 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0026_auto_20201026_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.ManyToManyField(blank=True, null=True, to='lms_app.Subject'),
        ),
    ]
