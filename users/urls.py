# Django imports
from django.urls import path
from django.contrib.auth.views import LogoutView
# Local imports
from .views import CustomLogin, CustomSignup, UserDetail

urlpatterns = [
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', CustomSignup.as_view(), name='signup'),
    path('profile/<int:pk>/', UserDetail.as_view(), name='profile'),
]
