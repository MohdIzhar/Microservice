from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="producturl"),
    path('new', views.new),
    path('addtocart/',views.addtocart, name="addtocarturl")
]