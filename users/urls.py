# Django imports
from django.urls import path
from . import views

urlpatterns = [
    path('user-list/', views.userList, name='users'),
]
