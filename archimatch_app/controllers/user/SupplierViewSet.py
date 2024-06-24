from rest_framework import viewsets
from ...serializers import SupplierSerializer
from ...serializers.utils.BankCardSerialize import BankCardSerializer
from ...serializers.utils.ArchitectPPSerializer import ArchitectPPSerializer
from ...models import Supplier,ArchimatchUser

from archimatch_app.models.utils.Otp import Otp
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from archimatch_app.services.ArchitectService import ArchitectService
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
import mimetypes
from django.http import HttpResponse
import random
from django.template.loader import render_to_string
from archimatch_project import settings
from archimatch_app.services.utils import send_email_with_template
from django.template.loader import render_to_string
from archimatch_app.services.utils import send_email_with_template

class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class=SupplierSerializer
    
    
    queryset = Supplier.objects.all()
    # permission_classes = (IsAuthenticated,)


    def create(self,request):
        print(request.data)
        data = request.data
        email= data.get('email')
        if ArchimatchUser.objects.filter(email=email).exists():
            return Response({"message":"email exsite déja"}, status=status.HTTP_400_BAD_REQUEST)
        
        new_user = ArchimatchUser.objects.create(email=email,user_type="Supplier")
        new_supplier = Supplier.objects.create(user = new_user)
        reset_link = f"http://localhost:3000/supplierVisitor/CreatePassword/{new_user.id}"  
        html_content = render_to_string(template_name="reset_password_client.html", context={'reset_link': reset_link})
        send_email_with_template(
                        data.get("email"),
                        "Reset Password",
                        html_content,
                        settings.COMMON_IMAGES
                    )

        
        return Response({"message":"invitation is sent"}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'], url_path='update_supplier_details')
    def update_supplier_details(self,request):
        print(request.data)
        data = request.data
        user_id = data.get("user_id")
        current_user = ArchimatchUser.objects.get(id=user_id)
        current_user.phone_number = data.get("phone_number")
        current_user.save()
        current_supplier = Supplier.objects.get(user_id=user_id)
        current_supplier.company_name=data.get("society")
        current_supplier.chosen_spec=data.get("chosen_spec")
        current_supplier.address = data.get("adresse")
        current_supplier.save()
        
        

        
        return Response({"message":"invitation is sent"}, status=status.HTTP_200_OK)

    


    # ## Send verification Code for email
    # @action(detail=False, methods=['POST'], url_path='verify_email')
    # def architect_verify_email(self, request):
    #     print(request.data)
    #     data = request.data
    #     arch_id = data.get("id")
    #     email = data.get("email")
    #     architect = Architect.objects.get(user_id=arch_id)
    #     print(email)
    #     if ArchimatchUser.objects.filter(email=email).exclude(id=arch_id).exists() :
    #         return Response({"message": "This E-mail is used"}, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         otp_code = str(random.randint(100000, 999999))
    #         Otp.objects.create(user_id=architect.user,code=otp_code)
            
    #         html_content = render_to_string(template_name="Architect_email_verify.html", context={'OTP_code': otp_code})

    #         send_email_with_template(
    #             email,
    #             "Email Verification",
    #             html_content,
    #             settings.COMMON_IMAGES
    #         )
    #     response_data = {
    #             'message': 'email sent successfully'            }
    #     return Response(response_data, status=status.HTTP_200_OK)


      ## Update Information de base 
   