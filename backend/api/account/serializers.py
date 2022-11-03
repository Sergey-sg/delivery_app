from rest_framework import serializers

from backend.apps.account.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'is_active', 'created', 'updated', 'phone_number', 'photo', 'img_alt', 'address']
        read_only_field = ['is_active', 'created', 'updated']
