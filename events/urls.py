from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.list, name="events_list"),
    path('details/', views.details, name="events_details"),
]