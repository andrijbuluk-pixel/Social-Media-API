from rest_framework import serializers
from media_system.models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "image",
            "post",
            "like_count",
            "comment_count"

        )

    @staticmethod
    def get_like_count(obj):
        return obj.post_like.count()

    @staticmethod
    def get_comment_count(obj):
        return obj.comment_post.count()


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "post",
            "user",
            "text",
        )
        read_only_fields = ("user",)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            "id",
            "post",
            "user",
        )
        read_only_fields = ("user",)