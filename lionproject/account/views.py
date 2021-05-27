from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = RegisterForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")#유효성검사에 통과된 클린한 데이터
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)#인증받기
            if user is not None:
                login(request, user)

        return redirect("home") 

    else: 
        form =RegisterForm()#폼하나를 생성
        return render(request, 'login.html',{'form':form})#form을 'form'으로 보낸다.

def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
        return redirect('home')
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form })