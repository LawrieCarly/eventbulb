from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = ('information_home'))
]