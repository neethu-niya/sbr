# Generated by Django 3.0 on 2020-10-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0034_auto_20201028_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6, null=True),
        ),
    ]
