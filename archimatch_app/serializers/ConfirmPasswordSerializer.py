
from rest_framework import serializers

class PasswordConfirmSerializer(serializers.Serializer):
     new_password = serializers.CharField(max_length=128)
     confirm_password = serializers.CharField(max_length=128)

     def validate(self, data):
        if data.get('new_password') != data.get('confirm_password'):
            raise serializers.ValidationError("New password and confirmation password do not match")
        return data