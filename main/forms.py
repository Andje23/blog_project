from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        # fields = ("first_name", "last_name", "e_mail")
        # exclude = ("first_name", )

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Введите свое имя'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите вашу фамилию'}),
            "e-mail": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите вашу почту'}),
            "phone_number": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш номер телефона'}),
            "contact_message": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваше сообщение'}),
        }





