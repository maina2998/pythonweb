from django.conf.urls import url
from . import views
app_name ='Calendar'
urlpatterns = [
    url(r"list/", views.CalendarView.as_view(), name='calendar'),
    url(r"register_calendar/", views.event, name='register_calendar.html'),
    url("profile/<int:id>/", views.calendar_profile, name = "calendar_profile"),
    url("profile/int:id/", views.edit_calendar, name="edit_calendar" ),

]