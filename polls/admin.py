# Django imports
from django.contrib import admin
# Local imports
from .models import Poll, PollVote, Vote

admin.site.register(Poll)
admin.site.register(Vote)
admin.site.register(PollVote)