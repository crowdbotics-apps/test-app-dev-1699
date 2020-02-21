from rest_framework import authentication
from users.models import Testing
from .serializers import TestingSerializer
from rest_framework import viewsets


class TestingViewSet(viewsets.ModelViewSet):
    serializer_class = TestingSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Testing.objects.all()
