from django.shortcuts import render, redirect
from .models import Blog, BlogComment, Contact
from .forms import ContactForm


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
    # if request.method == "POST":
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     e_mail = request.POST['e_mail']
    #     phone_number = request.POST['phone_number']
    #     contact_message = request.POST["contact_message"]
    #
    #     if len(first_name) < 2 or len(last_name) < 2 or len(e_mail) < 5 or len(phone_number) < 9 or len(contact_message) < 5:
    #         return redirect('home')
    #     else:
    #         save_data = Contact(first_name=first_name,
    #                             last_name=last_name,
    #                             e_mail=e_mail,
    #                             phone_number=phone_number,
    #                             contact_message=contact_message)
    #         save_data.save()
    #         return redirect('contact_us')

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, "main/contact_us.html", {"form": form})



