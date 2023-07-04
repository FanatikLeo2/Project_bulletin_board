import random

from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .forms import SignUpForm
from .models import OneTimeCode


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        form.instance.is_active = False
        return super().form_valid(form)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.is_active:
                user_auth = authenticate(username=username, password=password)
                if user_auth is not None:
                    login(request, user_auth)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Invalid password')
            else:
                if OneTimeCode.objects.filter(user=user).exists():
                    email_code = OneTimeCode.objects.get(user=user)
                else:
                    email_code = OneTimeCode.objects.create(code=random.randint(1000, 9999), user=user)

                send_mail(
                    subject='Account email confirmation',
                    message=f'Hi, your confirmation code "{email_code.code}"',
                    from_email=None,
                    recipient_list=[user.email],
                 )
                return redirect('user_login_code')
        else:
            return HttpResponse('Invalid username')
    return render(request, 'registration/login.html')


def login_with_code(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        code = request.POST['code']
        if OneTimeCode.objects.filter(code=code, user__username=username).exists():
            user = OneTimeCode.objects.get(user__username=username).user
            user.is_active = True
            user.save()
            user_auth = authenticate(username=username, password=password)
            if user_auth is not None:
                login(request, user_auth)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Invalid password')
        else:
            return HttpResponse('Invalid username or identefication code')
    return render(request, 'registration/activation_code_form.html')
