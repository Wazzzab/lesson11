from django.shortcuts import render, redirect, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_view(request):
    redirect_url = reverse('profile') 
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, "login.html")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return render(request, "login.html", context={"error": "Пользователь не найден"})

@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, "profile.html")

@login_required(login_url=reverse_lazy('login'))
def logout_view(request):
    logout(request)
    return redirect(reverse("login"))


