from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/events.html")
        else:
            messages.success(request, "There was an error loging in, try again")
            return redirect("login.html")
    else:
        return render(request, "authentication/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out")
    return redirect('login.html')

def register_user(request):
    if request.method=="POST":
        #form = UserCreationForm(request.POST)
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "sign up successful")
            return redirect("/events.html")
    else:
        #form = UserCreationForm()
        form = RegisterUserForm()
    return render(request, 'authentication/register_user.html',{"form":form})



