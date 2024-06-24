from rest_framework import serializers
from archimatch_app.models import BankCard

class BankCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCard
        fields = '__all__'