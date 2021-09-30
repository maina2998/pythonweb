from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from Calendar.models import Event

def home(request):
    

    return render(request,"home.html",{})
