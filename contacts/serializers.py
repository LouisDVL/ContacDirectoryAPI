from django.db import models
from django.db.models import fields
from .models import User, Email, PhoneNumber
from rest_framework import serializers


class EmailViewSerialized(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('id', 'email', 'is_active')


class PhoneNumberViewSerialized(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ('id', 'number', 'is_active')


class UserSerialized(serializers.ModelSerializer):
    def to_representation(self, instance):
        self.fields['email'] = EmailViewSerialized(many=True, read_only=True)
        self.fields['phoneNumber'] = PhoneNumberViewSerialized(
            many=True, read_only=True)
        return super().to_representation(instance)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phoneNumber')


class UserViewSerialized(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class EmailSerialized(serializers.ModelSerializer):
    def to_representation(self, instance):
        self.fields['user'] = UserViewSerialized(read_only=True)
        return super().to_representation(instance)

    class Meta:
        model = Email
        fields = ('id', 'email', 'is_active', 'user')


class PhoneNumberSerialized(serializers.ModelSerializer):
    user = UserViewSerialized(many=False, required=False)

    class Meta:
        model = PhoneNumber
        fields = ('id', 'number', 'is_active', 'user')
