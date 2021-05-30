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
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'forms-group__input'}),
            'first_name': forms.TextInput(attrs={'class': 'forms-group__input'}),
            'last_name': forms.TextInput(attrs={'class': 'forms-group__input'}),
            'password1': forms.PasswordInput(attrs={'class': 'forms-group__input'}),
            'password2': forms.PasswordInput(attrs={'class': 'forms-group__input'}),

        }