from rest_framework import serializers

from calendarApp.models import AppUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id', 'login', 'password', 'email')
