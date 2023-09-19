from django.urls import path
from django.contrib.auth.decorators import login_required
from dictonary.views import *

urlpatterns = [
    path('', login_required(HomePage.as_view()), name='home'),
    path('add_dictionary/', CreateDictionary.as_view(), name='add_dict'),
    path('wordbook/<str:wordbook_title>', ShowDictionary.as_view(), name='show_dict'),
    path('delete/<str:wordbook_title>', DeleteDictionary.as_view(), name='delete_dict'),
    path('update/<str:wordbook_title>', UpdateDictionary.as_view(), name='update_dict'),

    path('new_word/<str:wordbook_title>', CreateWord.as_view(), name='add_word'),
    path('delete_word/<str:wordbook_title>/<str:word_pk>', DeleteWord.as_view(), name='delete_word'),
    path('update_word/<str:wordbook_title>/<str:word_pk>', UpdateWord.as_view(), name='update_word'),

]
