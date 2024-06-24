from rest_framework import serializers
from archimatch_app.models import Realization,RealizationImage
from archimatch_app.serializers.utils.RealizationImageSerializer import RealizationImageSerializer
from archimatch_app.serializers.CategorySerializer import CategorySerializer

class RealizationSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=False)
    categorie = serializers.SerializerMethodField(read_only=False)
    class Meta:
        model = Realization
        fields = '__all__'
    
    def get_images(self,obj):
        images = RealizationImage.objects.filter(realization=obj)
        serializer = RealizationImageSerializer(images,many=True)
        return serializer.data
    
    # @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_categorie(self, obj):
        categorie = obj.categorie
        return CategorySerializer(categorie, many=False).data