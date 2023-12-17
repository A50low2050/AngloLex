from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.views.generic.list import MultipleObjectMixin

from .models import Dictionary, Word
from .forms import DictionaryForm, WordForm
from .mixins import GetObjectMixin
from .utils import translator_word


class HomePage(ListView):
    paginate_by = 3
    template_name = 'dictionary/home.html'
    context_object_name = 'dictionaries'
    extra_context = {'title': 'Home'}

    def get_queryset(self):
        sort_dictionary = self.request.GET.get('sort_dictionary', '')

        if sort_dictionary == 'alphabetically':
            self.request.session['sort'] = 'title'
        if sort_dictionary == 'recent_saving':
            self.request.session['sort'] = '-time_create'

        get_sort = self.request.session.get('sort', None)
        return Dictionary.objects.filter(user=self.request.user).order_by(get_sort)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        search_query = self.request.GET.get('search_dict', '')

        context['search_query'] = search_query

        if search_query:
            context['dictionaries'] = Dictionary.objects.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query))

        return context


class CreateDictionary(CreateView):
    form_class = DictionaryForm
    model = Dictionary
    template_name = 'dictionary/add_dictonary.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Create Dictionary'}

    def form_valid(self, form):
        dictionary = form.save(commit=False)
        dictionary.user = self.request.user
        dictionary.save()
        return super(CreateDictionary, self).form_valid(form)


class ShowDictionary(GetObjectMixin, DetailView, MultipleObjectMixin):
    model = Dictionary
    pk_url_kwarg = 'pk'
    template_name = 'dictionary/show_dictionary.html'
    context_object_name = 'dictionary'

    def get_context_data(self, **kwargs):

        object_list = Dictionary.objects.all()
        context = super(ShowDictionary, self).get_context_data(object_list=object_list, **kwargs)

        context['title'] = self.kwargs['wordbook_title']

        wordbook_title = self.kwargs['wordbook_title']
        context['dictionary'] = Dictionary.objects.filter(title=wordbook_title).first()

        dictionary = get_object_or_404(Dictionary, title=wordbook_title)
        words_list = Word.objects.filter(dictionary=dictionary)
        paginator = Paginator(words_list, 7)
        page_number = self.request.GET.get("page")

        context['paginator'] = paginator
        context['page_obj'] = paginator.get_page(page_number)

        search_query = self.request.GET.get('search_word', '')
        context['search_query'] = search_query

        if search_query:
            context['page_obj'] = words_list.filter(
                Q(word__icontains=search_query) | Q(translate_word__icontains=search_query))

            context['paginator'] = None

        return context


class DeleteDictionary(GetObjectMixin, DeleteView):
    model = Dictionary
    template_name = 'dictionary/confirm_delete.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'wordbook_title'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = self.kwargs['wordbook_title']

        wordbook_title = self.kwargs['wordbook_title']
        context['dictionary'] = Dictionary.objects.filter(title=wordbook_title).first()

        return context


class UpdateDictionary(GetObjectMixin, UpdateView):
    form_class = DictionaryForm
    model = Dictionary
    pk_url_kwarg = 'pk'
    template_name = 'dictionary/update_dictionary.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super(UpdateDictionary, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = self.kwargs['wordbook_title']

        return context


class CreateWord(GetObjectMixin, CreateView, DetailView):
    form_class = WordForm
    model = Dictionary
    template_name = 'words/add_word.html'

    def form_valid(self, form):
        wordbook_title = self.kwargs['wordbook_title']
        dictionary = Dictionary.objects.filter(title=wordbook_title).first()
        create_word = form.data['word']
        lang = form.data['lang']

        translate_word = translator_word(word=create_word, lang=lang)

        new_word, created = Word.objects.get_or_create(
            word=create_word,
            translate_word=translate_word,
            dictionary=dictionary
        )

        return HttpResponseRedirect(f'/wordbook/{wordbook_title}/{dictionary.pk}')


class DeleteWord(DeleteView):
    model = Word
    template_name = 'dictionary/show_dictionary.html'
    pk_url_kwarg = 'word_pk'
    context_object_name = 'dictionary'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        word_pk = self.kwargs['word_pk']
        word = Word.objects.filter(pk=word_pk).delete()

        wordbook_title = self.kwargs['wordbook_title']
        context['dictionary'] = Dictionary.objects.filter(title=wordbook_title).first()

        dictionary = Dictionary.objects.filter(title=wordbook_title).first()

        words_list = Word.objects.filter(dictionary=dictionary)
        paginator = Paginator(words_list, 8)
        page_number = self.request.GET.get("page")

        context['paginator'] = paginator
        context['page_obj'] = paginator.get_page(page_number)

        return context


class UpdateWord(UpdateView):
    form_class = WordForm
    model = Word
    pk_url_kwarg = 'word_pk'
    template_name = 'words/update_word.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        word_pk = self.kwargs['word_pk']
        context['word'] = Word.objects.get(id=word_pk)

        return context

    def form_valid(self, form):
        wordbook_title = self.kwargs['wordbook_title']
        dictionary = Dictionary.objects.filter(title=wordbook_title).first()

        create_word = form.data['word']
        lang = form.data['lang']

        translate_word = translator_word(word=create_word, lang=lang)

        word_pk = self.kwargs['word_pk']
        get_word = Word.objects.filter(id=word_pk)
        get_word.update(word=create_word, translate_word=translate_word, dictionary=dictionary)

        return HttpResponseRedirect(f'/wordbook/{wordbook_title}/{dictionary.pk}')
