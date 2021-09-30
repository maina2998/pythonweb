from django.urls import path
from .views import edit_trainer, register_trainer, trainer_profile, trainer_list

urlpatterns =[
    path("register/", register_trainer, name="register_trainer"),
    path("list/", trainer_list, name="trainer_list"),
    path("profile/<int:id>/", trainer_profile, name = "trainer_profile"),
    path("profile/int:id/", edit_trainer, name="edit_trainer" ),
]