# Django imports
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Local imports
from .models import Poll


class PollList(LoginRequiredMixin, ListView):
    model = Poll
    context_object_name = 'polls'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['polls'] = context['polls'].filter(user=self.request.user)
        return context

class PollDetail(DetailView):
    model = Poll
    context_object_name = 'poll'

class PollCreate(LoginRequiredMixin, CreateView):
    model = Poll
    fields = '__all__'
    success_url = reverse_lazy('polls')

class PollUpdate(LoginRequiredMixin, UpdateView):
    model = Poll
    fields = '__all__'
    success_url = reverse_lazy('polls')

class PollDelete(LoginRequiredMixin, DeleteView):
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('polls')