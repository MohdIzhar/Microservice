import login
from os import name
from django.urls import path
from .views import index, register, logincheck

urlpatterns = [
    path('', index, name='welcome'),
    path('login/', logincheck, name='login'),
    path('register/', register, name='register')
    ]