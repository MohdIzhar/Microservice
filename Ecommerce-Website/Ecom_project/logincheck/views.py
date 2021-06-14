from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
import regex as re

def login(request):
    context = {}
    context['loginform'] = LoginForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("producturl")
        else:
            messages.error(
                request, "User is not registered or credentials dont match")
            return redirect("loginurl")

    return render(request, "login.html", context)


def register(request):
    context = {}
    context['registerform'] = RegisterForm()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        pattern = "^([a-zA-Z0-9]|\.|\_|\-)+[@]([a-zA-Z0-9]|\.|\_|\-)+[.]([a-zA-Z0-9]|\.|\_|\-){2,3}$"

        valid = re.search(pattern, email)

        if not valid:
            messages.error(request, "Email entered is invalid")
            return redirect("registerurl")
            
        if password != confirm_password:
            messages.error(request, "Password don't match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.success(request, "User registered sucessfully!")
        return redirect("registerurl")

    return render(request, "register.html", context)
