from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from User.serializers import (
    CreateUserSerializer,
    AvatarSerializer,
)


class CreateUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = CreateUserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class AvatarUploadView(generics.UpdateAPIView):
    serializer_class = AvatarSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
