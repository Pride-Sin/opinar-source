# Django imports
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
# Local imports
from .forms import SignupForm
from .models import CustomUserManager

class CustomLogin(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('polls')

def custom_signup(request):
    context = {}
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = CustomUserManager.create_user(email=email, password=raw_password)
            login(request, user)
            return redirect('polls')
        else:
            context['signup_form'] = form
    else: #GET request
        form = SignupForm()
        context['signup_form'] = form
    return render(request, 'users/signup.html', context)