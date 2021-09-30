from rest_framework import routers, urlpatterns
from .views import StudentViewSet, TrainerViewSet,CourseViewSet
from django.urls.conf import include,path

router = routers.DefaultRouter()
router.register("students/", StudentViewSet),
router.register("trainers/", TrainerViewSet),
router.register("courses/", CourseViewSet),



urlpatterns =[
    path("", include(router.urls)),
    
]