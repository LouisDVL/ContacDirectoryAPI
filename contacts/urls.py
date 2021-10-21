from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import UserViewSets, EmailViewSets, PhoneNumberViewSets

router = routers.DefaultRouter()
router.register(r"Users", UserViewSets)
router.register(r"Emails", EmailViewSets)
router.register(r"PhoneNumbers", PhoneNumberViewSets)

urlpatterns = [
    path('', include(router.urls))
]
