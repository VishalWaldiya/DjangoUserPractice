from django.urls import path
from .views import SignUp,change_password,profile_update

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('password/', change_password, name='change_password'),
    path('profile_update/', profile_update, name='profile_update'),
]
