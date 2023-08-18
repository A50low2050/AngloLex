from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics, viewsets

from dictonary.models import Dictionary
from .serializer import DictionarySerializer


class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer


# class DictionaryApi(generics.ListCreateAPIView):
#     queryset = Dictionary.objects.all()
#     serializer_class = DictionarySerializer
#
#
# class DictionaryDetailApi(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Dictionary.objects.all()
#     serializer_class = DictionarySerializer
