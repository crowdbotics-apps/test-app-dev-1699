from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TestingViewSet, UserViewSet

router = DefaultRouter()
router.register("testing", TestingViewSet)
router.register("user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
