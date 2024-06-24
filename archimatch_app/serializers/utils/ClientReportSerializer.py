from rest_framework import serializers
from archimatch_app.models import ClientReport
from archimatch_app.serializers.user.ClientSerializer import ClientSerializer
from archimatch_app.serializers.utils.ReportsSerializer import ReportSerializer

class ClientReportSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    reports = ReportSerializer(many=True)  
    class Meta:
        model = ClientReport
        fields = '__all__'