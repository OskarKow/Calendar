from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'users', views.get_users, name='users'),
    path(r'authentication', views.authentication, name='authentication'),
    path(r'registration', views.registration, name='registration'),
    path(r'^.*', TemplateView.as_view(template_name="home.html"), name="home")
]
