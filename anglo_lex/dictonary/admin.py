from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Dictionary, Word


class WordBookAdmin(admin.ModelAdmin):
    model = Dictionary
    list_display = ['id', 'title', 'description']
    # prepopulated_fields = {"slug": ("title",)}
    # list_display = [field.name for field in Dictionary._meta.get_fields()]


class WordAdmin(admin.ModelAdmin):
    model = Word
    # list_display = ('word', 'translate_word', 'world_book')
    list_display = [field.name for field in Word._meta.get_fields()]


admin.site.register(Dictionary, WordBookAdmin)
admin.site.register(Word, WordAdmin)
