from django.db import models
from django.urls import reverse
import uuid


class Dictionary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20, db_index=True, unique=True)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_dict', kwargs={'wordbook_title': self.title, 'pk': self.id})

    class Meta:
        ordering = ['-time_create']


class Word(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    word = models.CharField(max_length=40, db_index=True)
    translate_word = models.CharField(max_length=40, db_index=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    dictionary = models.ForeignKey('Dictionary', on_delete=models.CASCADE)

    def __str__(self):
        return self.word

    class Meta:
        ordering = ['-time_create']
