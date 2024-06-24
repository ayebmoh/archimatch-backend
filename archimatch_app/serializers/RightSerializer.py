from rest_framework import serializers
from archimatch_app.models import Right

class RightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Right
        fields = '__all__'