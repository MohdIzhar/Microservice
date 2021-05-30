from django.db import models

# Create your models here.
class RegisterUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)