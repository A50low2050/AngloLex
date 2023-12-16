from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class DictionaryForm(forms.ModelForm):
    title = forms.CharField(label='Title',
                            error_messages={
                                'required': 'Please, enter the new title dictionary'
                            },
                            widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    description = forms.CharField(label='Description',
                                  widget=forms.Textarea(attrs={'class': 'form-control form-control-lg',
                                                               'rows': 3}), required=False)

    class Meta:
        model = Dictionary
        fields = ['title', 'description']


class WordForm(forms.ModelForm):
    word = forms.CharField(label='Word',
                           error_messages={
                               'required': 'Please, enter the new title word'
                           },
                           widget=forms.TextInput(attrs={'class': 'form-control form-control-lg mb-2'}))

    class Meta:
        model = Word
        fields = ['word']
