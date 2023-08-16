from django.urls import path
from api.views import *

urlpatterns = [
    path('api/v1/get_dictionary', DictionaryApi.as_view(), name='api'),
    path('api/v1/dictionary_detail/<int:pk>/', DictionaryDetailApi.as_view(), name='api_detail'),

]
