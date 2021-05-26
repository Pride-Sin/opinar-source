# Django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
# Local imports
from .models import Poll
class PollList(ListView):
    model = Poll
    context_object_name = 'polls'