from rest_framework import generics

from User.models import User
from User.serializers import (
    RegisterSerializers,
    LoginSerializers,
    UserDetailSerializer,
)


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers


class LoginUser(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializers


class UserDetail(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
