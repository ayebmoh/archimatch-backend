from rest_framework import serializers
from archimatch_app.models import ArchitectType


class ArchitectTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ArchitectType
        fields = '__all__'