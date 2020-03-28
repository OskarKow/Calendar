import django
import django.shortcuts

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world !!! <strong>PG ETI 2020</strong>")
