# Generated by Django 3.2.5 on 2021-09-09 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_passport_photo_student_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
