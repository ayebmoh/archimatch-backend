from rest_framework import serializers
from archimatch_app.models import Admin
from rest_framework_simplejwt.tokens import RefreshToken
from archimatch_app.serializers.user.ArchimatchUserSerializer import ArchiMatchUserSerializer
from archimatch_app.serializers.RightSerializer import RightSerializer
from drf_spectacular.utils import extend_schema_field




class AdminSerializer(serializers.ModelSerializer):
    user = ArchiMatchUserSerializer(required=True)
    rights = serializers.SerializerMethodField(method_name='get_rights')

    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_rights(self, obj):
        all_rights = obj.rights.all()
        return RightSerializer(all_rights, many=True).data

    class Meta:
        model = Admin
        fields = '__all__'