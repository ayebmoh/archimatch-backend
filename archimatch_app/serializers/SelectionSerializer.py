from rest_framework import serializers
from archimatch_app.models import Selection
from archimatch_app.serializers.user.ArchitectSerializer import ArchitectSerializer
from archimatch_app.serializers.AnnouncementSerializer import AnnouncementSerializer
from drf_spectacular.utils import extend_schema_field


class SelectionSerializer(serializers.ModelSerializer):
    announcement = AnnouncementSerializer()
    architect = ArchitectSerializer()
    interested_architects = serializers.SerializerMethodField(method_name='get_interested_architects')

    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_interested_architects(self, obj):
        all_architects = obj.interested_architects.all()
        return ArchitectSerializer(all_architects, many=True).data
    class Meta:
        model = Selection
        fields = '__all__'
   