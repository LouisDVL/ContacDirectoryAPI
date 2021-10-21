from rest_framework import viewsets
from .models import User, Email, PhoneNumber
from .serializers import UserSerialized, EmailSerialized, PhoneNumberSerialized

# Create your views here.


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialized


class EmailViewSets(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerialized


class PhoneNumberViewSets(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerialized
