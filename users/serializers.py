from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'is_staff',
            'is_superuser',
            'is_authenticated'
        ]

    def create(self, validated_data):
        # print(validated_data)
        password = validated_data.get('password')
        validated_data['password'] = make_password(password)
        # print(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        validated_data['password'] = make_password(password)
        print(validated_data)
        return super().update(instance, validated_data)

