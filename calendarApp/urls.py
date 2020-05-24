from django.urls import path, include

from . import views

from rest_framework import routers
from calendarApp.calendar.users.viewsets.UserViewSet import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='AppUser')

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index, name='index'),
]