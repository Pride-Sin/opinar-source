# Django imports
from django.urls import path
# Local imports
from .views import PollCreate, PollList, PollUpdate, PollDelete, poll_overview, vote

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls'),
    path('poll/overview/<int:poll_id>/', poll_overview, name='poll-overview'),
    path('poll/new/', PollCreate.as_view(), name='poll-new'),
    path('poll/update/<int:pk>/', PollUpdate.as_view(), name='poll-update'),
    path('poll/delete/<int:pk>/', PollDelete.as_view(), name='poll-delete'),
    path('vote/<int:poll_id>/', vote, name='poll-vote'),
]
