from django.db import models
from .models import User, Email, PhoneNumber
from rest_framework import serializers


class UserSerialized(serializers.ModelSerializer):
    email = serializers.StringRelatedField(many=True)
    phoneNumber = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phoneNumber')


class EmailSerialized(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('email', 'is_active', 'user')


class PhoneNumberSerialized(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ('number', 'is_active', 'user')
