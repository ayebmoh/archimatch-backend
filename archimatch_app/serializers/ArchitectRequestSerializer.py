from rest_framework import serializers
from archimatch_app.models import ArchitectRequest

class ArchitectRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchitectRequest
        fields = '__all__'