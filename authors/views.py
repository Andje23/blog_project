from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

from main.models import Blog
from .forms import SingnupForm, LoginUserForm
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
        form = LoginUserForm(request, data=request.POST)
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
    form = LoginUserForm()
    return render(request, "authors/login.html", {"login_form": form})


def logOut(request):
    logout(request)
    messages.success(request, "Ты успешно вышел из системы.")
    return redirect('home')


def profile(request, user_name):
    user_related_data = Blog.objects.filter(author__username=user_name)
    contex = {
        "user_related_data": user_related_data
    }
    return render(request, "authors/profile.html", contex)
