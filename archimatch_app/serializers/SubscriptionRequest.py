from rest_framework import serializers
from archimatch_app.models.utils.SubscriptionRequest import SubscriptionRequest

class SubscriptionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionRequest
        fields = '__all__'