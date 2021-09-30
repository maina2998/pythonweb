from django.shortcuts import render,redirect
from .forms import StudentRegistrationForm
from .models import Student

def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = StudentRegistrationForm()
    return render(request,"register_student.html", {"form":form})                

def student_list(request):
    students =Student.objects.all()
    return render(request, "student_list.html", {"students":students})

def student_profile(request, id):    
    students = Student.objects.get(id = id)
    return render(request, "student_profile.html", {"student":students})

def edit_student(request, id):
    students =Student.objects.get(id = id)
    if request.method: "POST"
    form  = StudentRegistrationForm(request.Post, instance=students)
    if form.is_valid():
        form.save()
        return redirect("student_profile", id = students.id)

    else:
        form = StudentRegistrationForm(instance=students)
        return render(request, "edit_student.html", {"form":form})

