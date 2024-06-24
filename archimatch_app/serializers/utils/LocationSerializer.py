from rest_framework import serializers
from archimatch_app.models.utils import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'