from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics

from dictonary.models import Dictionary
from .serializer import DictionarySerializer


class DictionaryApi(generics.ListCreateAPIView):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer


class DictionaryDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer

# class DictionaryApi(APIView):
#     def get(self, request, **kwargs):
#         dictionary = Dictionary.objects.all()
#         return Response({'wordbooks': DictionarySerializer(dictionary, many=True).data})
#
#     def post(self, request):
#         serializer = DictionarySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': request.data})
#
#     def put(self, request, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT is not allowed "})
#         try:
#             instance = Dictionary.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object is not exists"})
#
#         serializer = DictionarySerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"update_info": serializer.data})
#
#     def delete(self, request, **kwargs):
#         pk = kwargs.get("pk", None)
#         title = request.data["title"]
#         if not pk:
#             return Response({'error': 'Method DELETE not allowed'})
#
#         try:
#             instance = Dictionary.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({'error': 'Object is not exists'})
#
#         return Response({'success': f"dictionary {title} success delete"})



