from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from main.models import Blog
from .forms import SingnupForm, LoginUserForm, PasswordChangingForm, EditUserProfileForm, UserPublicDetailsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class singUp(SuccessMessageMixin, generic.CreateView):
    form_class = SingnupForm
    template_name = "authors/register.html"
    success_url = reverse_lazy('login')
    success_message = "Пользователь был создан, пожалуйста, войдите под своим именем пользователя и паролем"

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Пожалуйста, введите данные должным образом.")
        redirect('home')


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


class logOut(LoginRequiredMixin, generic.View):
    login_url = 'login'

    def get(self, request):
        logout(request)
        messages.success(request, "Пользователь вышел из системы")
        return redirect('home')


class profile(LoginRequiredMixin, generic.View):
    model = Blog
    login_url = 'login'
    template_name = "authors/profile.html"

    def get(self, request, user_name):
        user_related_data = Blog.objects.filter(author__username=user_name)
        context = {
            "user_related_data": user_related_data
        }
        return render(request, self.template_name, context)


class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    login_url = 'login'
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, "authors/password_change_success.html")


class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    form_class = EditUserProfileForm
    login_url = 'login'
    template_name = "authors/edit_user_profile.html"
    success_url = reverse_lazy('home')
    success_message = "Пользователь обновлен"

    def get_object(self):
        return self.request.user

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Пожалуйста, введите данные должным образом.")
        redirect('home')


class DeleteUser(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = User
    login_url = 'login'
    template_name = "authors/delete_user_confirm.html"
    success_message = "Пользователь был удален"
    success_url = reverse_lazy('home')


class UpdatePublicDetails(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    form_class = UserPublicDetailsForm
    login_url = "login"
    template_name = "authors/edit_public_details.html"
    success_url = reverse_lazy('home')
    success_message = "Пользователь обновлен"

    def get_object(self):
        return self.request.user.userprofile

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Пожалуйста, введите данные должным образом.")
        redirect('home')
