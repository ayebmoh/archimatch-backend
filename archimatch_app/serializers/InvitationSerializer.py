from rest_framework import serializers
from archimatch_app.models import Invitation
from archimatch_app.serializers.user.ArchitectSerializer import ArchitectSerializer


from archimatch_app.serializers.AnnouncementSerializer import AnnouncementSerializer
from drf_spectacular.utils import extend_schema_field


class InvitationSerializer(serializers.ModelSerializer):
    # architect = ArchitectSerializer()
    
    
    class Meta:
        model = Invitation
        fields = '__all__'



class InvitationAdminSerializer(serializers.ModelSerializer):
    architect = ArchitectSerializer()
    
    class Meta:
        model = Invitation
        fields = '__all__'
   