# Django imports
import os
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import LoginView, redirect_to_login
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin
# Local imports
from .forms import SignupForm, UserForm
from .models import User


class CustomLogin(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('polls')


class CustomSignup(UserPassesTestMixin, CreateView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('polls')

    def form_valid(self, form):
        valid = super().form_valid(form)

        # Login the user
        login(self.request, self.object)
        
        return valid

    def test_func(self):
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        

class UserDetail(DetailView):
    model = User
    context_object_name = 'user'


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm 

    def get_success_url(self):
        # Added user pk to redirect to profile of the user
        user_id=self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': user_id})
