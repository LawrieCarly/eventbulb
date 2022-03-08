from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.list, name="events_list"),
    path('<int:id>/', views.details, name="details_page")

]