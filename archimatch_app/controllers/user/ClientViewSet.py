from rest_framework import viewsets
from ...serializers import ClientSerializer
from ...models import Client,ArchimatchUser
from archimatch_app.models import ArchitectType
from rest_framework.response import Response
from rest_framework import status
from archimatch_app.services import AdminService
from rest_framework.decorators import action
from django.template.loader import render_to_string
from archimatch_app.services.utils import send_email_with_template
from archimatch_project import settings
from archimatch_app.models import ArchimatchUser,Architect,Devis,Selection,Report,ArchiReport
from rest_framework.views import APIView
from archimatch_app.serializers.ResetPasswordSerializer import PasswordResetSerializer
from archimatch_app.serializers.ConfirmPasswordSerializer import PasswordConfirmSerializer
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class=ClientSerializer
    queryset = Client.objects.all()


    @action(detail=False, methods=['POST'], url_path='get_client')
    def get_client(self,request):
        
        data = request.data

        if "email" in data.keys():
            client = Client.objects.filter(user__email=request.data.get("email")).first()
            if client:
                serializer = ClientSerializer(client, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                if ArchimatchUser.objects.filter(email=data.get("email")).exists():
                    return Response({"message":"cet email ne correspond pas a un client"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    new_user = ArchimatchUser.objects.create(username=data.get("email"),email=data.get('email'),user_type="Client")
                    Client.objects.create(user=new_user)
                    reset_link = f"http://localhost:3000/clientVisitor/CreatePassword/{new_user.id}"  
                    html_content = render_to_string(template_name="reset_password_client.html", context={'reset_link': reset_link})
                    send_email_with_template(
                        data.get("email"),
                        "Reset Password",
                        html_content,
                        settings.COMMON_IMAGES
                    )

                error_message = {"message": "Un email vous a été envoyer pour creer votre compte"}
                return Response(error_message, status=status.HTTP_404_NOT_FOUND)
        else:
            client = Client.objects.filter(user__phone_number=request.data.get("phone_number")).first()
            if client:
                serializer = ClientSerializer(client, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                if ArchimatchUser.objects.filter(phone_number=data.get("phone_number")).exists():
                    return Response({"message":"ce numero de téléphone ne correspond pas a un client"}, status=status.HTTP_400_BAD_REQUEST)
                return Response({"message":"ce numero de téléphone ne correspond pas a un client"}, status=status.HTTP_404_NOT_FOUND)


    @action(detail=False, methods=['GET'], url_path='find_client_by_user/(?P<arch_id>\d+)')
    def find_client(self, request,arch_id=None):
        
        architect = Client.objects.get(user_id=arch_id)
        serializer = self.serializer_class(architect)
        response_data = {
                'message': 'client found successfully'  ,
                'client': serializer.data          }
        return Response(response_data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'], url_path='update_base_info')
    def update_base_info(self, request):
        print(request.data)
        data = request.data
        client_id = data.get("id")
        
        client = Client.objects.get(id=client_id)
        
        user = ArchimatchUser.objects.get(id=client.user.id)
        user.first_name = data.get("first_name")
        user.first_name=data.get("first_name")
        user.last_name=data.get("last_name")
        user.email=data.get("email")
        user.phone_number=data.get("phone_number")
        user.save()
        client.save()

        response_data = {
             'message': 'Informations updated successfully'            }
        return Response(response_data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'], url_path='update_password_client')
    def update_password(self, request):       
            print(request.data)
            data = request.data
            client_id = data.get("id")
            actual_password = request.data.get("actual_password")
            print(actual_password)
            client = Client.objects.filter(id=client_id).first()
            user = client.user
            print(user)
            if not check_password(actual_password,user.password) :
                return Response({'error': 'Actual password is not correct'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                new_password = data.get('new_password')
                confirm_password = data.get('confirm_password')
                print(new_password)
                print(confirm_password)
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'New password and confirmation password do not match'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['POST'], url_path='handle_devis')
    def handle_devis(self, request):

        
        data = request.data
        print("devis is:")
        print(request.data)
        architect_id = data.get("architect_id")
        seleciton_id = data.get("selection_id")
        devis_id = data.get("devis_id")
        action = data.get("action")
    
        architect = Architect.objects.get(id=architect_id)
        selection = Selection.objects.get(id=seleciton_id)
        devis = Devis.objects.get(id=devis_id)
    
        if action : 
            devis.status="Accepted"
            selection.architect = architect
            devis.save()
            selection.save()
            return Response({'message': 'you have accepted the devis'}, status=status.HTTP_200_OK)
        else :
            devis.status="Refused"
            devis.save()
           
            return Response({'message': 'you have refusd the devis'}, status=status.HTTP_200_OK)
        


    # def create(self, request):
    #     service = AdminService()
    #     return service.admin_create(request)
    @action(detail=False, methods=['POST'], url_path='signaler_architect')
    def signaler_architect(self, request):

        
        data = request.data
        print(request.data)
        architect_id = data.get("architect_id")
        client_id = data.get("client_id")
        
        description = data.get("description")
        architect = Architect.objects.get(id=architect_id)
        user = ArchimatchUser.objects.get(id=client_id)
        report = Report.objects.create(user=user,description=description)
        if ArchiReport.objects.filter(architect=architect).exists():
            archiReport = ArchiReport.objects.get(architect=architect)
        else :
            archiReport = ArchiReport.objects.create(architect=architect)
        archiReport.rep_count= archiReport.rep_count+1
        archiReport.reports.add(report)
        archiReport.save()
        
        return Response({'message': 'you have added an architect'}, status=status.HTTP_200_OK)
        


class ClientPasswordResetView(APIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data.get("email")
            user = ArchimatchUser.objects.filter(username=email).first()
            print(user.username)
            if not user:
                return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
            uidb64 = user.pk
            print(uidb64)
            reset_link = f"http://localhost:3000/clientVisitor/CreateNewPassword/{uidb64}"  
            html_content = render_to_string(template_name="reset_password_client.html", context={'reset_link': reset_link})

            send_email_with_template(
                email,
                "Reset Password",
                html_content,
                settings.COMMON_IMAGES
            )

            return Response({'message': 'Password reset email sent successfully.'}, status=status.HTTP_200_OK)
        
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClientPasswordConfirmView(APIView):
    serializer_class = PasswordConfirmSerializer

    def post(self, request, *args, **kwargs):
        
        try:
            print(request.data)
            uid = request.data.get("id")
            user = get_user_model().objects.get(pk=uid)
            print(user)
        except (TypeError, ValueError, OverflowError, ObjectDoesNotExist):
            user = None
        if not user :
            return Response({'error': 'Invalid UID'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(data=request.data, context={'user': user})
        if serializer.is_valid():
            new_password = serializer.validated_data.get('new_password')
            confirm_password = serializer.validated_data.get('confirm_password')
            print(new_password)
        
            print(confirm_password)
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'New password and confirmation password do not match'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)