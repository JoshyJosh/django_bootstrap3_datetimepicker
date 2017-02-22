from django.shortcuts import render
from calendar_events.models import Event

from django.template import loader
from django.http import HttpResponse


# Create your views here.
def index(request):
    events = Event.objects.all()
    template = loader.get_template('index.html')
    context = {
        'events': events
    }
    return HttpResponse(template.render(context, request))
