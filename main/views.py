from django.shortcuts import render
from django.http import HttpResponse


def blog_home(request):
    return render(request, "main/blog_home.html")


def blog_detail(request):
    return render(request, "main/blog_detail.html")


def profile(request):
    return render(request, "main/profile.html")


def contactUs(request):
    return render(request, "main/contact_us.html")