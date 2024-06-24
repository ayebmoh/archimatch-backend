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



class ArchitectSerializer(serializers.ModelSerializer):
    user = ArchiMatchUserSerializer(required=True)
    services = serializers.SerializerMethodField(method_name='get_services')
    realisations = serializers.SerializerMethodField(method_name='get_realisations')
    arch_type = serializers.SerializerMethodField(method_name='get_arch_type')
    comments = serializers.SerializerMethodField(method_name='get_comments')

    preference = serializers.SerializerMethodField(method_name='get_preference')
    subscription = serializers.SerializerMethodField(method_name='get_subscription')

    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_preference(self, obj):
        pref = obj.preference
        return PreferenceSerializer(pref, many=False).data
    
    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_subscription(self, obj):
        pref = obj.subscription
        return ArchiSubscriptionSerializer(pref, many=False).data
    
    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_comments(self, obj):
        comments = Comment.objects.filter(architect = obj)
        
        return CommentSerializer(comments, many=True).data

    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_services(self, obj):
        
        all_services = obj.services.all()
        return ArchiServicetypeSerializer(all_services, many=True).data
    
    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_realisations(self, obj):
        
        all_realisations = Realization.objects.filter(architect=obj)
        return RealizationSerializer(all_realisations, many=True).data
    
    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_arch_type(self, obj):
        arch_type = obj.arch_type
        return ArchitectTypeSerializer(arch_type, many=False).data
    
    class Meta:
        model = Architect
        fields = '__all__'