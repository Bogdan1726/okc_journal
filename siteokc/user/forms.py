from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class ContactForm(forms.Form):
    username = forms.CharField(label='Логін який був вказаний при реєстрації',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Електронна пошта яка була вказана при реєстрації',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логін',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логін',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Електронна пошта',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторіть пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Ім'я",
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Прізвище',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
