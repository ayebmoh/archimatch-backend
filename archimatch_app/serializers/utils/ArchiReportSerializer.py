from rest_framework import serializers
from archimatch_app.models import ArchiReport
from archimatch_app.serializers.user.ArchitectSerializer import ArchitectSerializer
from archimatch_app.serializers.utils.ReportsSerializer import ReportSerializer
class ArchiReportSerializer(serializers.ModelSerializer):
    architect = ArchitectSerializer()
    reports = ReportSerializer(many=True)  
    class Meta:
        model = ArchiReport
        fields = '__all__'