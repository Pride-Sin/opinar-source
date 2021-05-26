# Django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
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
    fields = ['question', 'organization', 'allow_anon', 'allow_comments', 'allow_results']
