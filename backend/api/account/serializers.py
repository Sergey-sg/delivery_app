from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'email',
                  'is_active', 'phone_number', 'photo', 'img_alt', 'address']
        read_only_field = ['is_active']
