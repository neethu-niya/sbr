# Generated by Django 3.0 on 2020-11-07 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0048_auto_20201107_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
