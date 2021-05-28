# Django imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
# Local imports
from .models import CustomUser

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']