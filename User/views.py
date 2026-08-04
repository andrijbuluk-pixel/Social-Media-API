from rest_framework import viewsets

from User.models import User
from User.serializers import (
    RegisterSerializers,
    LoginSerializers,
    UserDetailSerializer,
)


class RegisterUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers


class LoginUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializers


class UserDetail(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
