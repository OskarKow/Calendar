# Create your views here.

from django.http import HttpResponse, JsonResponse
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
