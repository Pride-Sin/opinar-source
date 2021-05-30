# Django imports
import os
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import login
# Local imports
from .forms import SignupForm
from .models import User

class CustomLogin(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('polls')


class CustomSignup(CreateView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('polls')

    def form_valid(self, form):
        valid = super().form_valid(form)

        # Login the user
        login(self.request, self.object)
        
        return valid


class UserDetail(DetailView):
    model = User
    context_object_name = 'user'


class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'organization', 'picture']   

    def get_success_url(self):
        # Added user pk to redirect to profile of the user
        user_id=self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': user_id})