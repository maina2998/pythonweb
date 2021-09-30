from django.shortcuts import render, redirect
from trainer.models import Trainer
from .forms import TrainerRegistrationForm

def register_trainer(request):
    if request.method == "POST":
        form = TrainerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = TrainerRegistrationForm()
    return render(request, "register_trainer.html", {"form":form})   

def trainer_list(request):
    trainers =Trainer.objects.all()
    return render(request, "trainer_list.html", {"trainers":trainers})  

def trainer_profile(request, id):    
    trainers= Trainer.objects.get(id = id)
    return render(request, "trainer_profile.html", {"trainer":trainers})

def edit_trainer(request, id):
    trainers =Trainer.objects.get(id = id)
    if request.method: "POST"
    form  = TrainerRegistrationForm(request.Post, instance=trainers)
    if form.is_valid():
        form.save()
        return redirect("trainer_profile", id = trainers.id)

    else:
        form = TrainerRegistrationForm(instance=trainers)
        return render(request, "edit_trainer.html", {"form":form})



