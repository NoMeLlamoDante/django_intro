from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {'form': form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html", {'form': form})


def profile_view(request):
    return render(request, 'users/profile.html', {})
