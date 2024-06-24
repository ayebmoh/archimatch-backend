from rest_framework import serializers
from archimatch_app.models import Devis

class DevisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devis
        fields = '__all__'