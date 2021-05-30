from django.contrib import messages
from django.http import response
from django.shortcuts import render
from .models import RegisterUser
import pymysql.cursors

def dbConnect():
    mydb = pymysql.connect(host="loginappdb", user="izhar", passwd="Redhat@1", database="newlogindb")
    cursor = mydb.cursor()
    sqlQuery = "select email,password from loginapp_registeruser;"
    cursor.execute(sqlQuery)
    result = {}
    for q in cursor:
        result[q[0]] = q[1]
    return result 

def index(request):
    return render(request, 'welcome.html')

def logincheck(request):
    result = dbConnect()
    if request.method == "POST":
        email = request.POST["email"]
        entered_password = request.POST["password"]
        
        original_password = result.get(email, None)
        
        if len(email) == 0 or len(entered_password) == 0:
            messages.error(request, "Fields are empty!")
        elif email not in result:
            messages.error(request,"Email entered is invalid or not registered")
        elif email in result and entered_password != original_password:
            messages.error(request,"Password entered is incorrect!")
        else:
            messages.success(request,"Congratulations you logged in successfully!")
            
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        result = dbConnect()
        user = RegisterUser()
        
        user.name = request.POST["username"]
        user.email = request.POST["email"]
        user.password = request.POST["password"]
        user.cpassword = request.POST["cpassword"]
        
        if user.email in result:
            messages.error(request, "Email already exist!")
        elif user.password != user.cpassword:
            messages.error(request, "Password Don't match!")
        elif user.email == '' or user.name == '':
            messages.error(request, 'Some fields are empty!')
        else:
            messages.success(request, 'User Registered Successfully!')
            user.save()
            
    return render(request, 'register.html')
        
