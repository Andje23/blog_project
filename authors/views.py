from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy

from main.models import Blog
from .forms import SingnupForm, LoginUserForm, PasswordChangingForm, EditUserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.views import generic


# def singUp(request):
#     if request.method == "POST":
#         form = SingnupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Ваш акаунт создан успешно.")
#             new_user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password1']
#             )
#             login(request, new_user)
#             return redirect('home')
#         else:
#             messages.error(request, "Error")
#     else:
#         form = SingnupForm()
#     return render(request, "authors/register.html", {'form': form})


class singUp(generic.CreateView):
    form_class = SingnupForm
    template_name = "authors/register.html"
    success_url = reverse_lazy('login')


# def logIn(request):
#     if request.method == "POST":
#         form = LoginUserForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f"Вы успешно вошли в систему {username}.")
#                 return redirect('home')
#             else:
#                 messages.error(request, 'ОШЫБКА')
#         else:
#             messages.error(request, "Имя пользователя или пароль неверны.")
#     form = LoginUserForm()
#     return render(request, "authors/login.html", {"login_form": form})

class logIn(generic.View):
    form_class = LoginUserForm
    template_name = "authors/login.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
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
        return render(request, "authors/login.html", {"form": form})


# def logOut(request):
#     logout(request)
#     messages.success(request, "Ты успешно вышел из системы.")
#     return redirect('home')


class logOut(generic.View):
    def get(self, request):
        logout(request)
        return redirect('home')


# def profile(request, user_name):
#     user_related_data = Blog.objects.filter(author__username=user_name)
#     contex = {
#         "user_related_data": user_related_data
#     }
#     return render(request, "authors/profile.html", contex)

class profile(generic.View):
    model = Blog
    template_name = "authors/profile.html"

    def get(self, request, user_name):
        user_related_data = Blog.objects.filter(author__username=user_name)
        context = {
            "user_related_data": user_related_data
        }
        return render(request, self.template_name, context)


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, "authors/password_change_success.html")


class UpdateUserView(generic.UpdateView):
    form_class = EditUserProfileForm
    template_name = "authors/edit_user_profile.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
