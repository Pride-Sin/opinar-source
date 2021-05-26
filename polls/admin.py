# Django imports
from django.contrib import admin
# Local imports
from .models import Poll

admin.site.register(Poll)
