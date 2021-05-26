from django.urls import path
from .views import PollList

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls'),
]
