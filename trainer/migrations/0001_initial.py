# Generated by Django 3.2.5 on 2021-08-26 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12, null=True)),
                ('last_name', models.CharField(max_length=12, null=True)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('phone_number', models.PositiveIntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('profile_photo', models.ImageField(upload_to='images/')),
                ('languages', models.CharField(choices=[('ki', 'Kinyarwanda'), ('E', 'English'), ('K', 'kiswahili')], max_length=6, null=True)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Others')], max_length=6, null=True)),
                ('training_day', models.CharField(max_length=12, null=True)),
                ('date_joined', models.DateField(null=True)),
                ('bio', models.TextField(null=True)),
                ('contract', models.FileField(null=True, upload_to='')),
                ('date_hired', models.DateField(null=True)),
            ],
        ),
    ]
