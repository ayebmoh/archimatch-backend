from rest_framework import viewsets
from ...serializers import AdminSerializer
from ...models import Admin,ArchimatchUser
from rest_framework.response import Response
from rest_framework import status
from archimatch_app.services import AdminService
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password
from archimatch_app.services.utils import send_email_with_template
from archimatch_project import settings
from django.template.loader import render_to_string


class AdminViewSet(viewsets.ModelViewSet):
    serializer_class=AdminSerializer
    queryset = Admin.objects.all()
    
    def create(self, request):
        service = AdminService()
        return service.admin_create(request)


    @action(detail=False, methods=['POST'], url_path='update')
    def admin_update(self, request):
        print(request.data)
        data = request.data
        admin_id = data.get("id")
        rights = data.get("rights", [])
        user_data = data.get("user")
        print(rights)
        handled_rights = AdminService.process_rights(rights)

       
        admin = Admin.objects.get(id=admin_id)
        print(admin)

        check= user_data.get('email')
        
        
        if Admin.objects.filter(user__email=check).exclude(id=admin.id):
            return Response({"message": "email existe deja"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            admin.user.email = user_data.get("email")
            admin.user.first_name = user_data.get("first_name")
            admin.user.last_name = user_data.get("last_name")
            admin.user.save()

            admin.rights.clear()
            admin.rights.add(*handled_rights)

            admin.save()

            response_data = {
              'message': 'Admin updated successfully',
              'admin_id': admin.id
           }
            return Response(response_data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'], url_path='payment_in_progress')
    def admin_Relance(self, request):
            data = request.data
            email = data.get('email') 
            html_content = render_to_string(template_name="subscriptionRequest.html")

            send_email_with_template(
                email,
                "Demande D'abonnement",
                html_content,
                settings.COMMON_IMAGES
            )

            return Response({'message': 'Email sent successfully.'}, status=status.HTTP_200_OK)
    


    @action(detail=False, methods=['POST'], url_path='prolonger_selection')
    def prolonger_selection(self,request):
        service = AdminService()
        return service.prolonger_selection(request)
   
    @action(detail=False, methods=['GET'], url_path='architect_reports')
    def get_architect_reports(self,request):
        service = AdminService()
        return service.View_ArchiReports()
    
    @action(detail=False, methods=['GET'], url_path='client_reports')
    def get_client_reports(self,request):
        service = AdminService()
        return service.View_ClientReports()
    
    @action(detail=False, methods=['GET'], url_path='reports')
    def get_reports(self,request):
        service = AdminService()
        return service.view_reports()
    
    @action(detail=False, methods=['GET'], url_path='report_by_archireport/(?P<id>\d+)')
    def view_archireportdesc(self, request,id=None):

        service = AdminService()
        return service.view_archireports_descriptions(request,id=id)
    
    @action(detail=False, methods=['GET'], url_path='report_by_clientreport/(?P<id>\d+)')
    def view_reportdesc(self, request,id=None):

        service = AdminService()
        return service.view_clientreports_descriptions(request,id=id)
    



    @action(detail=False, methods=['GET'], url_path='comment_reports')
    def get_comment_reports(self,request):
        service = AdminService()
        return service.View_CommentReport()
    

    @action(detail=False, methods=['GET'], url_path='report_by_comment/(?P<id>\d+)')
    def report_by_comment(self, request,id=None):

        service = AdminService()
        return service.report_by_comment(request,id=id)
    