from rest_framework import serializers
from apps.users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration. Password is write-only."""

    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["id", "email", "password", "role"]
        read_only_fields = ["id", "role"]

    def create(self, validated_data):
        # Use create_user so password is hashed properly
        user = User.objects.create_user(
            username=validated_data["email"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    """Public user representation — no password, no hash."""

    class Meta:
        model = User
        fields = ["id", "email", "role"]
