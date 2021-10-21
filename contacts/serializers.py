from django.db import models
from .models import User, Email, PhoneNumber
from rest_framework import serializers


class UserSerialized(serializers.ModelSerializer):
    email = serializers.StringRelatedField(many=True, required=False)
    phoneNumber = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phoneNumber')


class EmailSerialized(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False, required=False)

    class Meta:
        model = Email
        fields = ('id', 'email', 'is_active', 'user')


class PhoneNumberSerialized(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ('id', 'number', 'is_active', 'user')
