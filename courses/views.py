from django.shortcuts import render, redirect
from courses.models import Courses
from .forms import CoursesRegistrationForm

def register_courses(request):
    if request.method == "POST":
        form = CoursesRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = CoursesRegistrationForm()
    return render(request, "register_courses.html", {"form":form})  

def courses_list(request):
    courses=Courses.objects.all()
    return render(request, "courses_list.html", {"courses":courses})                  

def courses_profile(request, id):    
    courses = Courses.objects.get(id = id)
    return render(request, "courses_profile", {"courses":courses})

def edit_courses(request, id):
    courses =Courses.objects.get(id = id)
    if request.method: "POST"
    form  = CoursesRegistrationForm(request.Post, instance=courses)
    if form.is_valid():
        form.save()
        return redirect("courses_profile", id = courses.id)

    else:
        form = CoursesRegistrationForm(instance=courses)
        return render(request, "edit_courses.html", {"form":form})
