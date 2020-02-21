from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TestingViewSet

router = DefaultRouter()
router.register("testing", TestingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
