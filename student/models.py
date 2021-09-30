from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=12, null=True)
    last_name = models.CharField(max_length=12, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    date_of_birth =models.DateField(null=True)
    student_id= models.CharField(max_length=16, null=True)
    email =models.EmailField(null=True)
    phone_number =models.PositiveIntegerField(null=True)
    parent_names =models.CharField(max_length=12, null=True)
    parents_number = models.PositiveIntegerField( null=True)
    registration_number =models.PositiveSmallIntegerField(null=True)
    medical_report = models.FileField(upload_to="documents/",null=True)
    class_name =models.CharField(max_length=5, null=True)
    room_number =models.CharField(max_length=4, null=True)
    mentor_names =models.CharField(max_length=12, null=True)
    profile_photo =models.ImageField(upload_to ="media/images",null=True,blank =True)
    big_sister =models.CharField(max_length=10, null=True)
    laptop_serial_number = models.CharField(max_length=20, blank=True, null= True)
   
    def full_name(self):
            return f"{self.first_name} {self.last_name}"
 
   
