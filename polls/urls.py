from django.urls import path
from .views import PollList, PollDetail

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls'),
    path('vote/<int:pk>/', PollDetail.as_view(), name='vote'),
]
