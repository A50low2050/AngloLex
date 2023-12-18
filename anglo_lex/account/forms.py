from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
    password1 = forms.CharField(min_length=1, label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control mb-4'}))
    password2 = forms.CharField(label='Repeat Your Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control mb-4'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
    password = forms.CharField(min_length=1, label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control mb-4'}))

    class Meta:
        model = User

