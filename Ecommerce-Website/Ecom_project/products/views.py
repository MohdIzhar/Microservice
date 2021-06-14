from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Product
from django.contrib import messages

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def addtocart(request):
    if request.user.is_authenticated:
        return redirect('producturl')
    else:
        messages.error(
                request, "Please Register User or Login to access products")
        return redirect('producturl')

def new(request):
    return HttpResponse("New Page")