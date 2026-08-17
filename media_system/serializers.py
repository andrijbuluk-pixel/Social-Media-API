from rest_framework import serializers
from media_system.models import Post, Comment, Like, Hashtag


class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    hashtag = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "image",
            "post",
            "hashtag",
            "like_count",
            "comment_count",
            "published_at",
            "is_published"
        )

        read_only_fields = ("is_published",)

    @staticmethod
    def added_hashtag(post):
        for hashtag in set(post.post.split()):
            if hashtag.startswith("#"):
                new_hashtag = Hashtag.objects.get_or_create(hashtag=hashtag)
                post.hashtag.add(new_hashtag[0])

    def get_hashtag(self, obj):
        return obj.hashtag.values_list("hashtag", flat=True)

    @staticmethod
    def get_like_count(obj):
        return obj.post_like.count()

    @staticmethod
    def get_comment_count(obj):
        return obj.comment_post.count()

    @staticmethod
    def get_post_count(obj):
        return obj.post_count.count()

    def create(self, validated_data):
        return super().create(validated_data)


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
