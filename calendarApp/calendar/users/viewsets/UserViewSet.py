from rest_framework import viewsets

from calendarApp.calendar.users.entities.serializers.UserSerializer import UserSerializer
from calendarApp.models import AppUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer
