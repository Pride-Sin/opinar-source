# Django imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
# Local imports
from .models import User

class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'forms-group__input', 'type':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'forms-group__input', 'type':'password'}),
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'forms-group__input'}),
            'first_name': forms.TextInput(attrs={'class': 'forms-group__input'}),
            'last_name': forms.TextInput(attrs={'class': 'forms-group__input'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'organization', 'picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'forms-group__input'}),
            'last_name': forms.TextInput(attrs={'class': 'forms-group__input'}),
            'organization': forms.TextInput(attrs={'class': 'forms-group__input'}),
            'picture': forms.FileInput(attrs={'class': 'forms-group__input', 'style': 'font-size: 1.1rem;'}),
        }