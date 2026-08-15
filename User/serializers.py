from rest_framework import serializers
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_field
from typing import List

from User.models import Follow


class UserSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "avatar",
            "first_name",
            "last_name",
            "phone_number",
            "gender",
            "email",
            "location",
            "description",
            "is_staff",
            "password",

            "followers",
            "following",
            "posts_count",
            "likes_count",
            "comments_count",
        )
        read_only_fields = (
            "is_staff", "follower",
            "following", "posts_count",
            "likes_count", "comments_count"
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 5,
                "style": {"input_type": "password"},
            }
        }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, set the password correctly and return it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user

    @extend_schema_field(int)
    def get_posts_count(self, obj) -> int:
        return obj.post_set.count()

    @extend_schema_field(int)
    def get_likes_count(self, obj) -> int:
        from media_system.models import Like
        return Like.objects.filter(post__post=obj).count()

    @extend_schema_field(int)
    def get_comments_count(self, obj) -> int:
        return obj.user_comment.count()

    @extend_schema_field(List[int])
    def get_followers(self, obj):
        return Follow.objects.filter(following=obj).values_list(
            "follower_id", flat=True
        )

    @extend_schema_field(List[int])
    def get_following(self, obj):
        return Follow.objects.filter(follower=obj).values_list(
            "following_id", flat=True
        )


class AvatarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "avatar",
        )


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "avatar",
            "first_name",
            "last_name",
        )
