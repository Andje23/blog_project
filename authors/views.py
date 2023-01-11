from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SingnupForm
from django.contrib.auth import authenticate, login, logout


def singUp(request):
    if request.method == "POST":
        form = SingnupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваш акаунт создан успешно.")
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('home')
        else:
            messages.error(request, "Error")
    else:
        form = SingnupForm()
    return render(request, "authors/register.html", {'form': form})


def logIn(request):
    return render(request, "authors/login.html")


def logOut(request):
    logout(request)
    messages.success(request, "Ты успешно вышел из системы.")
    return redirect('home')
