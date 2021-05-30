# Django imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
# Local imports
from .models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        