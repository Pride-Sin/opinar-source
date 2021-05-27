# Django imports
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Local imports
from .models import Poll


class PollList(ListView):
    model = Poll
    context_object_name = 'polls'


class PollDetail(DetailView):
    model = Poll
    context_object_name = 'poll'

class PollCreate(CreateView):
    model = Poll
    fields = '__all__'
    success_url = reverse_lazy('polls')

class PollUpdate(UpdateView):
    model = Poll
    fields = '__all__'
    success_url = reverse_lazy('polls')

class PollDelete(DeleteView):
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('polls')