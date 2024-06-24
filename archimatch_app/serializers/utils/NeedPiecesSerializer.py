from rest_framework import serializers
from archimatch_app.models import NeedPieces


class NeedPiecesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NeedPieces
        fields = '__all__'