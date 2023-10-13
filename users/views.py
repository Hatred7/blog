from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from .forms import RegisterForm, LoginForm


def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('users:log_in')
    return render(request, 'register.html', {'form': form})


def log_in(request):
    valid_user = True
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            login(request, form.get_user())
            return redirect('blog:home')
        valid_user = False
    return render(request, 'log_in.html', {'form': form, 'valid_user': valid_user})


def log_out(request):
    logout(request)
    return redirect('users:log_in')