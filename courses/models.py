from django.db import models

class Courses(models.Model):
    course_name = models.CharField(max_length=7, null=True)
    date_started =models.DateField(null=True)
    syllabus = models.TextField(null=True)
    course_id = models.CharField(max_length=3, null=True)
    course_code = models.CharField(max_length=7, null=True)
    course_duration = models.CharField(max_length=3, null=True)
