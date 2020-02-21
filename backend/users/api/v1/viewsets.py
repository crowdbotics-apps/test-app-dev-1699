from rest_framework import authentication
from users.models import Testing, User
from .serializers import TestingSerializer, UserSerializer
from rest_framework import viewsets


class TestingViewSet(viewsets.ModelViewSet):
    serializer_class = TestingSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Testing.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = User.objects.all()
