from rest_framework import serializers
from archimatch_app.models import ArchiSubscription

class ArchiSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchiSubscription
        fields = '__all__'