from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Вы успешно вошли в систему {username}.")
                return redirect('home')
            else:
                messages.error(request, 'ОШЫБКА')
        else:
            messages.error(request, "Имя пользователя или пароль неверны.")
    form = AuthenticationForm()
    return render(request, "authors/login.html", {"login_form": form})


def logOut(request):
    logout(request)
    messages.success(request, "Ты успешно вышел из системы.")
    return redirect('home')
