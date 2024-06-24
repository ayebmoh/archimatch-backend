from rest_framework import serializers
from archimatch_app.models.utils import Projectbudget

class ProjectbudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projectbudget
        fields = '__all__'