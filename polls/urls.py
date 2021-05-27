from polls.models import Poll
from django.urls import path
from .views import PollCreate, PollList, PollDetail, PollUpdate, PollDelete

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls'),
    path('vote/<int:pk>/', PollDetail.as_view(), name='poll-vote'),
    path('poll/new/', PollCreate.as_view(), name='poll-new'),
    path('poll/update/<int:pk>/', PollUpdate.as_view(), name='poll-update'),
    path('poll/delete/<int:pk>/', PollDelete.as_view(), name='poll-delete'),
]
