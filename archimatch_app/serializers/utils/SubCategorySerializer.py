from rest_framework import serializers
from archimatch_app.models.utils.SubCategory import SubCategory

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'