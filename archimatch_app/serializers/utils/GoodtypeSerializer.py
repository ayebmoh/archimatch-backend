from rest_framework import serializers
from archimatch_app.models.utils import Goodtype

class GoodtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goodtype
        fields = '__all__'