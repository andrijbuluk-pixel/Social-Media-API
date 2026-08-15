from django.utils.autoreload import is_django_path
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, request
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.authentication import JWTAuthentication

from User.serializers import (
    UserSerializer,
    AvatarUpdateSerializer,
    FollowerSerializer,
)

from User.models import User, Follow


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class AvatarUploadView(generics.UpdateAPIView):
    serializer_class = AvatarUpdateSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserSearchView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('first_name', 'last_name', 'email')


class FollowPostUser(APIView):
    queryset = Follow.objects.all()
    serializer_class = FollowerSerializer

    def get(self, request, pk):
        is_following = Follow.objects.filter(
            follower=request.user,
            following_id=pk
        ).exists()
        return Response({"is_follower": is_following})

    def post(self, request, pk):
        user = User.objects.get(pk=pk)

        if request.user == user:
            return Response(status=status.HTTP_204_NO_CONTENT)

        follow, created = Follow.objects.get_or_create(follower=request.user, following=user)

        if created:
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)

        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FollowingView(ListAPIView):
    serializer_class = FollowerSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pk = User.objects.filter(
            following__follower=self.request.user,
        )
        return pk


class FollowerView(ListAPIView):
    serializer_class = FollowerSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pk = User.objects.filter(
            follower__following=self.request.user,
        )
        return pk