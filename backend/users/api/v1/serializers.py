from rest_framework import serializers
from users.models import Testing


class TestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = "__all__"
