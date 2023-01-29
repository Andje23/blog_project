from django import forms
from .models import Contact, Blog
from ckeditor.widgets import CKEditorWidget


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Введите свое имя'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите вашу фамилию'}),
            "e_mail": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите вашу почту'}),
            "phone_number": forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите ваш номер телефона'}),
            "contact_message": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваше сообщение'}),
        }


class CreateBlogForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        exclude = ('post_date', 'slug')
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id': 'author', 'type': 'hidden'}),
            'mini_description': forms.Textarea(attrs={'class': 'form-control'})
        }


class UpdateBlogForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        exclude = ('post_date', 'slug')
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id': 'author', 'type': 'hidden'}),
            'mini_description': forms.Textarea(attrs={'class': 'form-control'})
        }
