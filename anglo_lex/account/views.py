import requests
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .models import Users
from .forms import UserRegisterForm, UserLoginForm
from .tokens import create_jwt_pair_for_user


class SignUp(CreateView):
    model = Users
    template_name = 'account/sign_up.html'
    form_class = UserRegisterForm

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']

        api_url = 'http://127.0.0.1:8000/api/v1/account/signup/'
        response = requests.post(api_url, data={
            'email': email,
            'username': username,
            'password': password,
        })

        if response.status_code == 201:
            return redirect(reverse_lazy('login'))

        return super().post(request, *args, **kwargs)


class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['username']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            create_jwt_pair_for_user(user)

        else:
            messages.error(request, 'username or password not correct')
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('home')
