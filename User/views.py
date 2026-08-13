from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.authentication import JWTAuthentication

from User.serializers import (
    CreateUserSerializer,
    AvatarSerializer,
    UserSerializer,
)

from User.models import User


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


class UserSearchView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('first_name', 'last_name', 'email')
