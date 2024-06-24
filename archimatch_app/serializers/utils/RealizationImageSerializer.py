from rest_framework import serializers
from archimatch_app.models.RealizationImage import RealizationImage

class RealizationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealizationImage
        fields = '__all__'
