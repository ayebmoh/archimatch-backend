
from archimatch_app.models import ArchitectType
from archimatch_app.models import ArchitectRequest
from archimatch_app.serializers import ArchitectRequestSerializer
from rest_framework.response import Response
from rest_framework import status


class ArchitectRequestService:
    serializer_class = ArchitectRequestSerializer
    def architect_type_process(self,architect_type,data):
        filtered_instances = ArchitectType.objects.filter(display=architect_type)
        instance = None
        if not filtered_instances.exists():
            instance = ArchitectType.objects.create(display=architect_type)
            data["architect_type"]= instance.id
           
        else:
            instance = filtered_instances.first()
            data["architect_type"]= instance.id
        
        return data, instance
    
    def architect_request_create(self,request):
        data = request.data
        if ArchitectRequest.objects.filter(email=data["email"]).exists():
            return Response({"message": "email existe deja"}, status=status.HTTP_400_BAD_REQUEST)
        print(data)
        architect_type = data.get("architect_type")
        
        handled_data,instance = self.architect_type_process(architect_type,data)
        
        serializer = self.serializer_class(data = handled_data, partial=True)
        if serializer.is_valid():
            handled_data["architect_type"]= instance
            ArchitectRequest.objects.create(**handled_data)

        response_data = {
            'message': 'Object created successfully with custom status code',
            
        }
        return Response(response_data, status=status.HTTP_201_CREATED)