from rest_framework import serializers

from User.models import User


class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
        )

        extra_kwargs = {"password": {"write_only": True}}


class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )

        extra_kwargs = {"password": {"write_only": True}}


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "avatar",
            "username",
            "first_name",
            "last_name",
            "gender",
            "email",
            "phone_number",
            "is_active",
            "location",
            "description",
            "password",
        )

        read_only_fields = ("is_active", )
        extra_kwargs = {"password": {"write_only": True}}
