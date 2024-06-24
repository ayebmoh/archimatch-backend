from rest_framework import serializers
from archimatch_app.models import ArchiServicetype


class ArchiServicetypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ArchiServicetype
        fields = '__all__'