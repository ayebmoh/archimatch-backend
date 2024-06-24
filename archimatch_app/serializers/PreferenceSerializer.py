from rest_framework import serializers
from archimatch_app.models import Preference
from rest_framework_simplejwt.tokens import RefreshToken
from archimatch_app.serializers.user.ArchimatchUserSerializer import ArchiMatchUserSerializer
from archimatch_app.serializers.utils.WorksurfaceSerializer import WorksurfaceSerializer
from archimatch_app.serializers.utils.WorktypeSerializer import WorktypeSerializer
from archimatch_app.serializers.utils.GoodtypeSerializer import GoodtypeSerializer
from archimatch_app.serializers.utils.ServicesSerializer import ServicesSerializer
from archimatch_app.serializers.utils.LocationSerializer import LocationSerializer
from archimatch_app.serializers.utils.ProjectbudgetSerializer import ProjectbudgetSerializer
from drf_spectacular.utils import extend_schema_field




class PreferenceSerializer(serializers.ModelSerializer):
    work_type = serializers.SerializerMethodField(method_name='get_work_type')
    good_type = serializers.SerializerMethodField(method_name='get_good_type')
    service = serializers.SerializerMethodField(method_name='get_service')
    location = serializers.SerializerMethodField(method_name='get_location')
    work_surface = serializers.SerializerMethodField(method_name='get_work_surface')
    project_budget = serializers.SerializerMethodField(method_name='get_project_budget')

    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_work_type(self, obj):
        all_work_types = obj.work_type.all()
        return WorktypeSerializer(all_work_types, many=True).data
    
    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_good_type(self, obj):
        all_good_types = obj.good_type.all()
        return GoodtypeSerializer(all_good_types, many=True).data
    
    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_service(self, obj):
        all_services = obj.service.all()
        return ServicesSerializer(all_services, many=True).data
    
    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_location(self, obj):
        all_locations = obj.location.all()
        return LocationSerializer(all_locations, many=True).data
    
    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_work_surface(self, obj):
        all_work_surfaces = obj.work_surface.all()
        return WorksurfaceSerializer(all_work_surfaces, many=True).data
    
    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_project_budget(self, obj):
        all_project_budgets = obj.project_budget.all()
        return ProjectbudgetSerializer(all_project_budgets, many=True).data

    class Meta:
        model = Preference
        fields = '__all__'