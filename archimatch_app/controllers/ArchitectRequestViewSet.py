from rest_framework import viewsets
from ..serializers import ArchitectRequestSerializer
from ..models import ArchitectRequest
from archimatch_app.models import ArchimatchUser,Architect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from archimatch_app.services import ArchitectRequestService
from django.contrib.auth.hashers import make_password
from archimatch_app.services.utils import send_email_with_template
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from archimatch_project import settings
from django.template.loader import render_to_string


class ArchitectRequestViewSet(viewsets.ModelViewSet):
    serializer_class=ArchitectRequestSerializer
    queryset = ArchitectRequest.objects.all()
    
    def create(self, request):
        service = ArchitectRequestService()
        return service.architect_request_create(request)
    

    @action(detail=False, methods=['POST'], url_path='handle_request')
    def handle_create_account_request(self,request):
        data = request.data
        request_id = data.get("id")
        architect_request = ArchitectRequest.objects.get(id=request_id)
        if (data.get('accept')):    
            architect_request.status='Accepted'
            architect_request.save()

            email = architect_request.email
            if ArchimatchUser.objects.filter(email=email).exists():
                return Response({"message": "email existe deja"}, status=status.HTTP_400_BAD_REQUEST)
            
            new_user = ArchimatchUser.objects.create(username=email, first_name=architect_request.first_name,email=email, password=make_password("Test123*"), last_name=architect_request.last_name,user_type="Architect")
            architect = Architect.objects.create(user=new_user,house_type=data.get("house_type"),work_type=data.get("work_type"),work_style=data.get("work_style"),categories=data.get("categories"),complexity=data.get("complexity"),arch_type=architect_request.architect_type)  
          
           #email part
            print(new_user.id)
            reset_link = f"http://localhost:3000/archVisitor/create_password/{new_user.id}"  
            html_content = render_to_string(template_name="architectrequest.html", context={'reset_link': reset_link})
            send_email_with_template(
                email,
                "Architect Account Creation",
                html_content,
                settings.COMMON_IMAGES
            )

            return Response({'message': 'Email sent successfully.'}, status=status.HTTP_200_OK)

        else :
            architect_request.status = "Refused"
            architect_request.save()

            # architect_type = data.get("architect_type")
        
        # handled_data,instance = self.architect_type_process(architect_type,data)
        
        # serializer = self.serializer_class(data = handled_data, partial=True)
        # if serializer.is_valid():
        #     handled_data["architect_type"]= instance
        #     ArchitectRequest.objects.create(**handled_data)

        response_data = {
            'message': 'Object created successfully with custom status code',
            
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

