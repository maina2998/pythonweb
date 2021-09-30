from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.serializers import Serializer
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from .serializer import StudentSerializer,TrainerSerializer,CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer