from rest_framework import serializers
from archimatch_app.models import Architect,Realization,ArchitectType,Comment
from archimatch_app.serializers.utils.ArchiServicetypeSerializer import ArchiServicetypeSerializer
from archimatch_app.serializers.user.ArchimatchUserSerializer import ArchiMatchUserSerializer
from archimatch_app.serializers.RealizationSerializer import RealizationSerializer
from archimatch_app.serializers.PreferenceSerializer import PreferenceSerializer
from archimatch_app.serializers.CommentSerializer import CommentSerializer
from archimatch_app.serializers.ArchiSubscriptionSerializer import ArchiSubscriptionSerializer
from drf_spectacular.utils import extend_schema_field
from archimatch_app.serializers.utils.ArchitectTypeSerializer import ArchitectTypeSerializer



class SupplierSerializer(serializers.ModelSerializer):
    user = ArchiMatchUserSerializer(required=True)
    
    class Meta:
        model = Architect
        fields = '__all__'