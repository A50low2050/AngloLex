from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class CreateDictionaryForm(forms.ModelForm):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    description = forms.CharField(label='Description',
                                  widget=forms.Textarea(attrs={'class': 'form-control form-control-lg',
                                                               'rows': 3}), required=False)

    class Meta:
        model = Dictionary
        fields = ['title', 'description']


class UpdateDictionaryForm(forms.ModelForm):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    description = forms.CharField(label='Description',
                                  widget=forms.Textarea(attrs={'class': 'form-control form-control-lg',
                                                               'rows': 7}), required=False)

    class Meta:
        model = Dictionary
        fields = ['title', 'description']


class CreateWordForm(forms.ModelForm):
    word = forms.CharField(label='Word',
                           widget=forms.TextInput(attrs={'class': 'form-control form-control-lg mb-2'}))

    class Meta:
        model = Word
        fields = ['word']


class UpdateWordForm(forms.ModelForm):
    word = forms.CharField(label='Word',
                           widget=forms.TextInput(attrs={'class': 'form-control form-control-lg mb-2'}))

    class Meta:
        model = Word
        fields = ['word']
