from django.shortcuts import render, get_object_or_404
from .models import Event

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
    # return render(request, 'events/list.html', {'events': events})