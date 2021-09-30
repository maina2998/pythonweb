# Generated by Django 3.2.5 on 2021-08-26 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12, null=True)),
                ('last_name', models.CharField(max_length=12, null=True)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('student_id', models.CharField(max_length=16, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.PositiveIntegerField(null=True)),
                ('parent_names', models.CharField(max_length=12, null=True)),
                ('parents_number', models.PositiveIntegerField(null=True)),
                ('registration_number', models.PositiveSmallIntegerField(null=True)),
                ('medical_report', models.FileField(null=True, upload_to='documents/')),
                ('class_name', models.CharField(max_length=5, null=True)),
                ('room_number', models.CharField(max_length=4, null=True)),
                ('mentor_names', models.CharField(max_length=12, null=True)),
                ('passport_photo', models.ImageField(null=True, upload_to='images/')),
                ('big_sister', models.CharField(max_length=10, null=True)),
                ('laptop_serial_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
