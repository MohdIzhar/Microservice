from django.contrib import admin
from .models import RegisterUser

class RegisterUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

admin.site.register(RegisterUser, RegisterUserAdmin)