# Django imports
from django.urls import path
from django.contrib.auth.views import LogoutView
# Local imports
from .views import CustomLogin, custom_signup

urlpatterns = [
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', custom_signup, name='signup')
]
