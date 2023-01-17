from django.shortcuts import render, redirect
from .models import Blog, BlogComment, Contact
from .forms import ContactForm
from django.contrib import messages
from django.views import generic


# def blog_home(request):
#     all_blogs = Blog.objects.all()
#     context = {'blogs': all_blogs}
#     return render(request, "main/blog_home.html", context)

class blog_home(generic.ListView):
    model = Blog
    template_name = "main/blog_home.html"


# def blog_detail(request, slug_url):
#     blog = Blog.objects.get(slug=slug_url)
#     all_blogs = Blog.objects.all().order_by('-post_date')[:10]
#     contex = {
#         'blog': blog,
#         'all_blogs': all_blogs,
#     }
#     return render(request, "main/blog_detail.html", contex)


class blog_detail(generic.DetailView):
    model = Blog
    template_name = "main/blog_detail.html"

# def contactUs(request):
#     # if request.method == "POST":
#     #     first_name = request.POST['first_name']
#     #     last_name = request.POST['last_name']
#     #     e_mail = request.POST['e_mail']
#     #     phone_number = request.POST['phone_number']
#     #     contact_message = request.POST["contact_message"]
#     #
#     #     if len(first_name) < 2 or len(last_name) < 2 or len(e_mail) < 5 or len(phone_number) < 9 or len(contact_message) < 5:
#     #         return redirect('home')
#     #     else:
#     #         save_data = Contact(first_name=first_name,
#     #                             last_name=last_name,
#     #                             e_mail=e_mail,
#     #                             phone_number=phone_number,
#     #                             contact_message=contact_message)
#     #         save_data.save()
#     #         return redirect('contact_us')
#
#     form = ContactForm()
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Ваша форма отправлена успешно")
#     else:
#         form = ContactForm()
#     return render(request, "main/contact_us.html", {"form": form})


class contactUs(generic.CreateView):
    form_class = ContactForm
    template_name = "main/contact_us.html"
    success_url = "/"