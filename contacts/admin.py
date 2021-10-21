from django.contrib import admin
from .models import User, Email, PhoneNumber


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'user')


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_active', 'user')


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(PhoneNumber, PhoneNumberAdmin)
