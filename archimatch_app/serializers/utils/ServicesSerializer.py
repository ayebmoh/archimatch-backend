from rest_framework import serializers
from archimatch_app.models.utils import Services

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'