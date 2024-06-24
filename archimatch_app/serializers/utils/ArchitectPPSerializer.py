from rest_framework import serializers
from archimatch_app.models.user.Architect import Architect
class ArchitectPPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Architect
        fields = ['architect_avatar']