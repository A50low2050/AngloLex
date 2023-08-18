from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Dictionary, Word

from .utils import translator_word


class WordBookAdmin(admin.ModelAdmin):
    model = Dictionary
    list_display = ['title', 'description', 'time_create']
    ordering = ('title', 'time_create',)
    list_display_links = ['title']
    search_fields = ('title', 'description',)
    readonly_fields = ('time_create',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description',)
        }),
        ('Time', {
            'fields': ('time_create',),
        }),
    )


class WordAdmin(admin.ModelAdmin):
    model = Word
    list_display = ['word', 'translate_word', 'time_create', 'dictionary']
    ordering = ('word', 'translate_word', 'time_create',)
    list_display_links = ['word']
    search_fields = ('word', 'translate_word',)
    fields = ('dictionary', 'word', 'translate_word', 'time_create',)
    readonly_fields = ('time_create', 'translate_word',)

    def save_model(self, request, obj, form, change):
        get_word = translator_word(word=obj.word, lang='en')
        obj.translate_word = get_word
        return obj.save()


admin.site.register(Dictionary, WordBookAdmin)
admin.site.register(Word, WordAdmin)
