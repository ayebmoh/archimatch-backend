from rest_framework import serializers
from archimatch_app.models import Report
from archimatch_app.serializers.user.ArchimatchUserSerializer import ArchiMatchUserSerializer

class ReportSerializer(serializers.ModelSerializer):
    user = ArchiMatchUserSerializer(required=True)

    class Meta:
        model = Report
        fields = '__all__'