from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Event

@login_required
def add_attending(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        request.user.profile.attending.add(event)
    return redirect("events_list")


@login_required
def remove_attending(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        request.user.profile.attending.remove(event)
    return redirect("events_list")

def dashboard(request,id):
    event = get_object_or_404(Event,id=id)
    return render(request, 'events/dashboard.html', {'event': event})


def details(request, id):
    eventFromDatabase = get_object_or_404(Event, id = id)
    return render(request, 'events/details.html', {'event': eventFromDatabase})

def list(request):

    filter_map = {
        'title' : 'title__icontains', 
        'is_free': 'cost__exact'
    }

    filters = {}

    for key, value in request.GET.items():
        filter_key = filter_map[key]
        if value: 
            filters[filter_key] = value

    eventsList = Event.objects.filter(**filters)
    return render(request, 'events/list.html', {'events': eventsList})

    # eventsList = Event.objects.filter(
    #     datetime__gte=today).filter(**filters).order_by('datetime')
    # return render(request, 'events/list.html', {'events': eventsList})