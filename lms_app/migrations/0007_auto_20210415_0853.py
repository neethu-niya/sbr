# Generated by Django 3.0 on 2021-04-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0006_doubt'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/image/'),
        ),
        migrations.AddField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/image/'),
        ),
    ]