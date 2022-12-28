from django.shortcuts import render
from .models import Blog, BlogComment


def blog_home(request):
    all_blogs = Blog.objects.all()
    context = {'blogs': all_blogs}

    return render(request, "main/blog_home.html", context)


def blog_detail(request, slug_url):
    blog = Blog.objects.get(slug=slug_url)
    all_blogs = Blog.objects.all().order_by('-post_date')[:10]
    contex = {
        'blog': blog,
        'all_blogs': all_blogs,
    }
    return render(request, "main/blog_detail.html", contex)


def profile(request):
    return render(request, "main/profile.html")


def contactUs(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        e_mail = request.POST['e_mail']
        phone_number = request.POST['phone_number']
        contact_message = request.POST["contact_message"]
    return render(request, "main/contact_us.html")
