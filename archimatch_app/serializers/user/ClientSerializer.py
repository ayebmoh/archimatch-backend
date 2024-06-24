from rest_framework import serializers
from archimatch_app.models import Client

from archimatch_app.serializers.user.ArchimatchUserSerializer import ArchiMatchUserSerializer




class ClientSerializer(serializers.ModelSerializer):
    user = ArchiMatchUserSerializer(required=True)
    class Meta:
        model = Client
        fields = '__all__'