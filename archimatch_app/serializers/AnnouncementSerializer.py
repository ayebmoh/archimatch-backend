from rest_framework import serializers
from archimatch_app.models import Announcement
from archimatch_app.serializers.user.ClientSerializer import ClientSerializer
from .utils import NeedPiecesSerializer, ArchitectTypeSerializer

class AnnouncementSerializer(serializers.ModelSerializer):
    client = ClientSerializer(required=True)
    need_pieces = NeedPiecesSerializer(required=True)
    architect_type = ArchitectTypeSerializer(required=True)
    class Meta:
        model = Announcement
        fields = '__all__'