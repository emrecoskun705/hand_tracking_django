from unittest import result
from rest_framework import serializers


class MLResponseSerializer(serializers.Serializer):
    result = serializers.IntegerField()
