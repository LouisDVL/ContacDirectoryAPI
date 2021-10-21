from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Email(models.Model):
    email = models.CharField(max_length=60)
    is_active = models.BooleanField()
    user = models.ForeignKey(User, related_name='email',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class PhoneNumber(models.Model):
    number = models.IntegerField()
    is_active = models.BooleanField()
    user = models.ForeignKey(
        User, related_name='phoneNumber', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)
