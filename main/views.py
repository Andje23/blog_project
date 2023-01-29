from django.shortcuts import render, redirect
from .models import Blog, BlogComment, Contact
from .forms import ContactForm, CreateBlogForm, UpdateBlogForm
from django.contrib import messages
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class blog_home(generic.ListView):
    model = Blog
    template_name = "main/blog_home.html"


class blog_detail(generic.DetailView):
    model = Blog
    template_name = "main/blog_detail.html"


class contactUs(SuccessMessageMixin, generic.CreateView):
    form_class = ContactForm
    template_name = "main/contact_us.html"
    success_url = "/"
    success_message = "Ваш запрос был успешно отправлен, мы свяжемся с вами в ближайшее время."

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Пожалуйста, внимательно заполните форму.")
        redirect('home')


class CreateBlog(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CreateBlogForm
    template_name = "main/create_blog.html"
    login_url = 'login'
    success_url = "/"
    success_message = "Ваш блог был создан"


class UpdateBlogView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Blog
    form_class = UpdateBlogForm
    template_name = "main/update_blog.html"
    login_url = 'login'
    success_url = "/"
    success_message = "Ваш блог был обновлен"
