from rest_framework import serializers
from archimatch_app.models import Comment
from archimatch_app.serializers.user.ClientSerializer import ClientSerializer

from archimatch_app.serializers.AnnouncementSerializer import AnnouncementSerializer
from drf_spectacular.utils import extend_schema_field


class CommentSerializer(serializers.ModelSerializer):
    Client = ClientSerializer()
    
    
    class Meta:
        model = Comment
        fields = '__all__'




   