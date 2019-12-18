from rest_framework import serializers
from data.models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['title', 'name', 'description']
