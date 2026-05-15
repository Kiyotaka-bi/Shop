from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ConfirmationCode
import random


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_active=False
        )

        code = str(random.randint(100000, 999999))

        ConfirmationCode.objects.create(
            user=user,
            code=code
        )

        print("CONFIRM CODE:", code)

        return user


class ConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField()