# Generated by Django 3.2.5 on 2021-09-01 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='passport_photo',
            new_name='profile_photo',
        ),
    ]
