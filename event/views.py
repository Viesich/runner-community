from django.shortcuts import render
from django.views import generic

from event.models import Event, Runner, EventRegistration


def index(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'event/index.html', context)


class RunnerListView(generic.ListView):
    pass
    # model = Runner
    # paginate_by = 10
    # template_name = 'runner_list.html'
    # context_object_name = 'registrations'
    #
    # def get_queryset(self):
    #     event_id = self.kwargs['event_id']
    #     return EventRegistration.objects.filter(event_id=event_id)
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['event'] = get_object_or_404(Event, id=self.kwargs['event_id'])
    #     return context


class RunnerDetailView(generic.DetailView):
    model = Runner


class RunnerCreateView(generic.CreateView):
    model = Runner
    template_name = "event/runner_form.html"
    fields = "__all__"

