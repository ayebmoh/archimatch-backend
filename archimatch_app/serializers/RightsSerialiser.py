from rest_framework import serializers
from archimatch_app.models.utils import Right

class RightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Right
        fields = '__all__'