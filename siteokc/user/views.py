from django.views import View

from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

# Create your views here.


def index(request):
    customer = User.objects.get(username=request.user.username)
    return render(request, 'user/profile.html', {'customer': customer, 'title': 'Профіль'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Користувач з такою адрессою эдектроної пошти вже зареєстрований')
            else:
                form.save()
                messages.success(request, 'Користувач успішно зареєстрований, тепер можете Авторизуватись')
                return redirect('login')
        else:
            messages.error(request, 'Помилка при реєстрації')
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Реєстрація',
        'form': form
    }
    return render(request, 'user/index.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Помилка при Авторизації')

    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизація',
        'form': form
    }
    return render(request, 'user/login_in.html', context)


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = 'user/password_reset_email.txt'
                    c = {
                        "email": user.email,
                        'domain': '10.104.10.171',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'okcdnipro@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
            else:
                messages.error(request, 'Користувача з такою поштою не знайдено')

    password_reset_form = PasswordResetForm()
    return render(request, 'user/password_reset.html',
                  context={"password_reset_form": password_reset_form, 'title': 'Відновлення паролю'})


def user_logout(request):
    logout(request)
    return redirect('login')
