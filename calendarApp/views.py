# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from calendarApp.calendar.users.entities.serializers.UserSerializer import UserSerializer
from calendarApp.models import AppUser


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
        data = {}
        try:
            data = AppUser.objects.get(login=request.GET['login'])
        except ObjectDoesNotExist:
            return JsonResponse(status=400, content='Login incorrect.', safe=False)

        password = request.GET['password']
        if data.password != password:
            return HttpResponse(status=400, content='The password is not correct.')
        else:
            serializer = UserSerializer(data, many=False)
            return HttpResponse(status=200, content=serializer.data)


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        try:
            AppUser.objects.get(login=request.POST['login'])
        except ObjectDoesNotExist:
            pass
        else:
            return HttpResponse(status=400, content='Given login already exists.')

        try:
            AppUser.objects.get(email=request.POST['email'])
        except ObjectDoesNotExist:
            pass
        else:
            return HttpResponse(status=400, content='Given e-mail already is signed to account.')

        user = AppUser(
            login=request.POST['login'],
            password=request.POST['password'],
            email=request.POST['email']
        )
        user.save()
        return HttpResponse(status=201, content='Account created successful.')

        return JsonResponse('Account created successful.', safe=False)
