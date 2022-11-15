from rest_framework import serializers
from ..account.serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password', 'is_active']

    def create(self, validated_data):
        try:
            user = get_user_model().objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = get_user_model().objects.create_user(**validated_data)  # type: ignore
        return user