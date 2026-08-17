from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from media_system.serializers import (
    PostSerializer,
    CreateCommentSerializer,
    LikeSerializer,
)

from media_system.models import Like, Post, Follow
from media_system.tasks import postponed_post_task


class CreatePostApi(generics.CreateAPIView):
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        published_at = serializer.validated_data.get('published_at')

        if published_at:
            post_instance = serializer.save(is_published=False)
            PostSerializer.added_hashtag(post_instance)

            transaction.on_commit(
                lambda: postponed_post_task.apply_async(
                    args=[post_instance.id],
                    eta=published_at,
                )
            )

        else:
            post_instance = serializer.save(is_published=True)
            PostSerializer.added_hashtag(post_instance)


class DetailPostApiCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        post_instance = serializer.save()
        PostSerializer.added_hashtag(post_instance)


class PostSearchApi(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["post",]
    filterset_fields = ["hashtag"]


class CreateCommentApi(generics.CreateAPIView):
    serializer_class = CreateCommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        user_following = Follow.objects.filter(follower=user).values_list("following", flat=True)

        return Post.objects.filter(user__in=user_following)


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
