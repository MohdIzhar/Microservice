from django.urls import path
from .views import login, register
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', login, name="loginurl"),
    path('login/', login, name="loginurl"),
    path('register/', register, name="registerurl"),
    path('logout/', LogoutView.as_view(), name="logouturl")
]
