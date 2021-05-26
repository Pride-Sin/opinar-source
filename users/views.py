# Django imports
from django.shortcuts import render
from django.http import HttpResponse

def userList(request):
    return HttpResponse('Users list response')

