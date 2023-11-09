from .models import Instrument
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class InstrumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instrument
        # the fields that should be included in the serialized output
        fields = ['name', 'description', 'image', 'price', 'quanity_available', 'brand', 'category', 'condition', 'created_at', 'updated_at']