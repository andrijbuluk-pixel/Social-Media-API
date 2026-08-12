from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

from media_system.serializers import (
    PostSerializer,
    CreateCommentSerializer,
    LikeSerializer,
)

from media_system.models import Like, Post


class CreatePostApi(generics.CreateAPIView):
    serializer_class = PostSerializer


class DetailPostApiCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class CreateCommentApi(generics.CreateAPIView):
    serializer_class = CreateCommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddLikeApi(APIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            like.delete()
            return Response({"detail": "Like removed"})
        return Response({"detail": "Like added"}, status=201)
