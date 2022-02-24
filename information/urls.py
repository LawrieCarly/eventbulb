from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='information_home'),
    path('django_meetup', views.django_meetup, name = 'meetup')
]