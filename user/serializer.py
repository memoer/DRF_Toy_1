from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    # full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            # "full_name",
            "email",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        password = validated_data.get("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    # def get_full_name(self, obj):
    #     if obj.first_name == "" and obj.last_name == "":
    #         return None
    #     return f"{obj.first_name}_{obj.last_name}"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={"input_type": "password"})


class LoginResultSerializer(serializers.Serializer):
    token = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)