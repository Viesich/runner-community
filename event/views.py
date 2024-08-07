from datetime import datetime

from django.db.models import Count
from django.shortcuts import render
from django.views import generic

from event.models import Event, Runner, EventRegistration


def index(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'event/index.html', context)


class EventListView(generic.ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event/event_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.annotate(participant_count=Count('events')).order_by('-date').distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_type'] = 'All Events'
        return context


class RunnerListView(generic.ListView):
    model = EventRegistration
    template_name = 'event/runner_list.html'
    context_object_name = 'registrations'

    def get_queryset(self):
        event_id = self.kwargs.get('event_id')
        return EventRegistration.objects.filter(event_id=event_id)


class RunnerDetailView(generic.DetailView):
    model = Runner


class RunnerCreateView(generic.CreateView):
    model = Runner
    template_name = "event/runner_form.html"
    fields = "__all__"

