from rest_framework import serializers
from archimatch_app.models.utils import Worksurface

class WorksurfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worksurface
        fields = '__all__'