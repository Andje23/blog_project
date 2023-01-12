from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя пользователя',
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
    class Meta:
        fields = ['username', 'password']


class SingnupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите свое имя'
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите свое имя'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите вашу фамилию'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите вашу почту'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите ваш пароль'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Повторите ваш пароль'
        })

    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
