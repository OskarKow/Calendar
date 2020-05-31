# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

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
            return JsonResponse(status=400, data='Login or password is invalid.', safe=False)

        password = request.GET['password']
        if data.password != password:
            return JsonResponse(status=400, data='Login or password is invalid')
        else:
            serializer = UserSerializer(data, many=False)
            return JsonResponse(status=200, data=serializer.data)


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        try:
            AppUser.objects.get(login=request.POST['login'])
        except ObjectDoesNotExist:
            pass
        else:
            return JsonResponse(status=400, content='Given login already exists.')

        try:
            AppUser.objects.get(email=request.POST['email'])
        except ObjectDoesNotExist:
            pass
        else:
            return JsonResponse(status=400, content='Account with that email already exists.')

        user = AppUser(
            login=request.POST['login'],
            password=request.POST['password'],
            email=request.POST['email']
        )
        user.save()
        return JsonResponse(status=201, content='Account created successfully.')
