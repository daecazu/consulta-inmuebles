"""reportes serializers"""

# Django REST framework

from rest_framework import serializers

# models imports
from inmuebles.models import Property
from inmuebles.models import Status


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('address', 'city', 'price', 'description', 'year')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('name', 'label')


class StatusHistorySerializer(serializers.Serializer):
    property = PropertySerializer()
    status = StatusSerializer()
