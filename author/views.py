from django.shortcuts import render


def singUp(request):
    return render(request, "authors/register.html")


def loginUp(request):
    return render(request, "authors/login.html")
