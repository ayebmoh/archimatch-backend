from rest_framework import serializers
from archimatch_app.models import CommentReport

from archimatch_app.serializers.utils.ReportsSerializer import ReportSerializer
from archimatch_app.serializers.CommentSerializer import CommentSerializer
class CommentReportSerializer(serializers.ModelSerializer):
    comment = CommentSerializer()
    reports = ReportSerializer(many=True)  
    class Meta:
        model = CommentReport
        fields = '__all__'