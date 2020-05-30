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
            return JsonResponse(False, safe=False)

        password = request.GET['password']
        if data.password != password:
            return JsonResponse({'response': 'The password is not correct. Elo'}, safe=False)
        else:
            serializer = UserSerializer(data, many=False)
            return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        try:
            AppUser.objects.get(login=request.POST['login'])
        except ObjectDoesNotExist:
            pass
        else:
            return JsonResponse('Given login already exists.', safe=False)

        try:
            AppUser.objects.get(email=request.POST['email'])
        except ObjectDoesNotExist:
            pass
        else:
            return JsonResponse('Given e-mail already is signed to account.', safe=False)

        user = AppUser(
            login=request.POST['login'],
            password=request.POST['password'],
            email=request.POST['email']
        )
        user.save()

        return JsonResponse('Account created successful.', safe=False)
