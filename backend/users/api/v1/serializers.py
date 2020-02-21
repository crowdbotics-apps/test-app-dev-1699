from rest_framework import serializers
from users.models import Testing, User


class TestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
