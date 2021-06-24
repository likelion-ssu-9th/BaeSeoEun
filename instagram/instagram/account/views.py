from account.forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form =AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("number")
            password= form.cleaned_data.get("password")
            user = authenticate(request=request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect("home",{'user':user})
    
    else:
        form = AuthenticationForm()
        return render(request, 'ssu_login.html',{'form': form})


def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
           user = form.save() 
           login(request, user)
        return redirect('home',{'user':user})
    else:
        form = RegisterForm()
        return render(request, 'signUp.html',{'form':form})