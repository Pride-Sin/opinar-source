# Django imports
from django.urls import path
from django.contrib.auth.views import LogoutView
# Local imports
from .views import CustomLogin, CustomSignup, UserDetail, UserUpdate

urlpatterns = [
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', CustomSignup.as_view(), name='signup'),
    path('profile/<int:pk>/', UserDetail.as_view(), name='profile'),
    path('profile/update/<int:pk>/', UserUpdate.as_view(), name='user-update'),
]
