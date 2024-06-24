from rest_framework import serializers
from archimatch_app.models.utils import Worktype

class WorktypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worktype
        fields = '__all__'