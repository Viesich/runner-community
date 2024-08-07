from django.shortcuts import render
from django.views import generic

from event.models import Event, Runner


def index(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'event/index.html', context)


class RunnerListView(generic.ListView):
    model = Runner
    paginate_by = 10

#
# class DriverDetailView(generic.DetailView):
#     model = RunnerUser


