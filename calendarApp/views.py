# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import json

from calendarApp.calendar.users.entities.serializers.UserSerializer import UserSerializer
from calendarApp.models import AppUser

import logging

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello, world !!! <strong>PG ETI 2020</strong>")


@csrf_exempt
def get_users(request):
    data = AppUser.objects.all()
    if request.method == 'GET':
        serializer = UserSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def authentication(request):
    if request.method == 'GET':
        try:
            data = AppUser.objects.get(login=request.GET['login'])
        except ObjectDoesNotExist:
            return JsonResponse(status=400, data='Login lub hasło jest nieprawidłowe.', safe=False)

        password = request.GET['password']
        if data.password != password:
            return JsonResponse(status=400, data='Login lub hasło jest nieprawidłowe.', safe=False)
        else:
            serializer = UserSerializer(data, many=False)
            return JsonResponse(status=200, data=serializer.data, safe=False)


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            AppUser.objects.get(login=body['login'])
        except ObjectDoesNotExist:
            pass
        else:
            return JsonResponse(status=400, data='Konto o tym loginie juz istnieje.', safe=False)

        try:
            AppUser.objects.get(email=body['email'])
        except ObjectDoesNotExist:
            pass
        else:
            return JsonResponse(status=400, data='Konto o tym emailu juz istnieje.', safe=False)

        user = AppUser(
            login=body['login'],
            password=body['password'],
            email=body['email']
        )
        user.save()
        return JsonResponse(status=201, data='Konto zostało utworzone! Możesz się zalogować', safe=False)
