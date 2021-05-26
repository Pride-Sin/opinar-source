# Django imports
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pollList(request):
    return HttpResponse('La vista esta funcionando')