from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def singUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Ваш акаунт создан успешно.")
        return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "authors/register.html", {'form': form})


def logIn(request):
    return render(request, "authors/login.html")
