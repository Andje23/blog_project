from django.shortcuts import render


def singUp(request):
    return render(request, "authors/register.html")


def logIn(request):
    return render(request, "authors/login.html")
