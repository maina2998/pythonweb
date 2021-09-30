from django import forms
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from datetime import date
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils.safestring import mark_safe
from .forms import EventForm

from .models import *
from .utils import Calender

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('day', None))
        calender = Calender(d.year, d.month)
        html_calender = calender.formatmonth(withyear=True)
        context['Calendar'] = mark_safe(html_calender)
        return context
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('Calendar:calender'))
    return render(request, 'register_calendar.html', {'form': form})

def calendar_profile(request, id):    
    Calendar = Event.objects.get(id = id)
    return render(request, "calendar_profile", {"calendar":Calendar})

def edit_calendar(request, id):
    Calendar =Event.objects.get(id = id)
    if request.method: "POST"
    form  = EventForm(request.Post, instance=Calendar)
    if form.is_valid():
        form.save()
        return redirect("calendar_profile", id = Calendar.id)

    else:
        form = EventForm(instance=Calendar)
        return render(request, "edit_calendar.html", {"form":form})    