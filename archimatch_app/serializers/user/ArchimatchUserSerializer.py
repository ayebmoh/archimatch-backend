from rest_framework import serializers
from archimatch_app.models import ArchimatchUser
from rest_framework_simplejwt.tokens import RefreshToken


class ArchiMatchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchimatchUser
        fields = ['username','first_name','last_name','email','phone_number','image',"user_type","id"]
    

class ArchiMatchUserTokenSerializer(ArchiMatchUserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ArchimatchUser
        fields = ['id','username','first_name','last_name','email','phone_number','image','token',"user_type"]
    
    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)