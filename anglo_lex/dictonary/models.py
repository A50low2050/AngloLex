from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Dictionary(models.Model):
    title = models.CharField(max_length=20, db_index=True, unique=True)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_dict', kwargs={'wordbook_title': self.title})

    class Meta:
        ordering = ['-time_create']


class Word(models.Model):
    word = models.CharField(max_length=40, db_index=True)
    translate_word = models.CharField(max_length=40, db_index=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    dictionary = models.ForeignKey('Dictionary', on_delete=models.CASCADE)

    def __str__(self):
        return self.word

    class Meta:
        ordering = ['-time_create']
