from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == "POST":
        uname = request.GET['name']
        password = request.GET['pass']
        print(password)
        # Authenticate
        user = authenticate(request, username=uname, password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request, "You  Have logged in successfully ")
            return redirect(request, 'home.html')
        else:
            messages.success(request, "There was an problem during login Please try again!!!")
    else:
        return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out.....")
    return render(request, 'home.html')

def register_user(request):
    return render(request, 'register.html', {})
