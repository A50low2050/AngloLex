from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from dictonary.models import Dictionary

from .serializer import (
    SignUpSerializer,
    SignInSerializer,
    DictionarySerializer
)


class DictionaryViewSet(ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer


class SignUpApiView(GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingInApiView(GenericAPIView):
    serializer_class = SignInSerializer
    permission_classes = []

    def post(self, request: Request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            response = {"message": "Success login"}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            response = {"message": "Invalid email or password"}
            return Response(data=response, status=status.HTTP_401_UNAUTHORIZED)
