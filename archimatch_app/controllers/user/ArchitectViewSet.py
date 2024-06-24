from rest_framework import viewsets
from ...serializers import ArchitectSerializer,ReceiptSerializer
from ...serializers.utils.BankCardSerialize import BankCardSerializer
from ...serializers.utils.ArchitectPPSerializer import ArchitectPPSerializer
from ...models import Architect,ArchimatchUser,ArchitectRequest,Subscription,ArchiSubscription,BankCard,Preference,Receipt,SubscriptionRequest,Announcement,Selection,Report,CommentReport,Comment

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


class ArchitectViewSet(viewsets.ModelViewSet):
    serializer_class=ArchitectSerializer
    bankcard_serializer=BankCardSerializer
    Archipp_serializer = ArchitectPPSerializer
    queryset = Architect.objects.all()
    # permission_classes = (IsAuthenticated,)



    


    ## Send verification Code for email
    @action(detail=False, methods=['POST'], url_path='verify_email')
    def architect_verify_email(self, request):
        print(request.data)
        data = request.data
        arch_id = data.get("id")
        email = data.get("email")
        architect = Architect.objects.get(user_id=arch_id)
        print(email)
        if ArchimatchUser.objects.filter(email=email).exclude(id=arch_id).exists() :
            return Response({"message": "This E-mail is used"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            otp_code = str(random.randint(100000, 999999))
            Otp.objects.create(user_id=architect.user,code=otp_code)
            
            html_content = render_to_string(template_name="Architect_email_verify.html", context={'OTP_code': otp_code})

            send_email_with_template(
                email,
                "Email Verification",
                html_content,
                settings.COMMON_IMAGES
            )
        response_data = {
                'message': 'email sent successfully'            }
        return Response(response_data, status=status.HTTP_200_OK)


      ## Update Information de base 
    @action(detail=False, methods=['POST'], url_path='update_base_info')
    def architect_update_base(self, request):
        print("aaaaaaaaaaaaaaaaa")
        print(request.data)
        data = request.data
        arch_id = data.get("id")
        email = data.get("email")
        otp_code = data.get('otp_code')
        architect = Architect.objects.get(user_id=arch_id)
        otp =Otp.objects.filter(user_id=arch_id).order_by('-created_at').first()
        print(type(otp.code))
        if(otp.code==int(otp_code)):
            
            Otp.objects.filter(user_id=architect.user).delete()
            architect.user.first_name = data.get("first_name")
            architect.user.last_name=data.get("last_name")
            architect.user.email=data.get("email")
            architect.bio=data.get("bio")
            architect.user.phone_number=data.get("phone_number")
            architect.user.save()
            architect.save()
            response_data = {
                'message': 'Informations updated successfully'            }
        else:
            response_data = {
                'message': 'Verification code is incorrect'            }            
            
        return Response(response_data, status=status.HTTP_200_OK)
    
    
    
    
        ## Update Information du Societe 
    @action(detail=False, methods=['POST'], url_path='update_company_info')
    def architect_update_company(self, request):
        print(request.data)
        print(request.FILES)
        data = request.data
        arch_id = data.get("id")
        
        architect = Architect.objects.get(user_id=arch_id)
        architect.company_name=data.get("company_name")
        architect.registration_number=data.get("registration_number")
        architect.company_logo= request.FILES.get("company_logo")
        architect.save()

        response_data = {
             'message': 'Informations updated successfully'            }
        return Response(response_data, status=status.HTTP_200_OK)
    
    ## Update Information de services 
    @action(detail=False, methods=['POST'], url_path='update_services_info')
    def set_services_info(self, request):
        print(request.data)
        data = request.data
        arch_id = data.get("id")
        services = data.get("services", [])
        print(services)

        handled_services = ArchitectService.process_services(services)

       
        architect = Architect.objects.get(user_id=arch_id)
        print(architect)
        architect.services.clear()
        architect.services.add(*handled_services)

        architect.save()

        response_data = {
              'message': 'Architect services updated successfully',
              'architect_id': architect.id
           }
        return Response(response_data, status=status.HTTP_200_OK)
    

## Update Bank card architect
    @action(detail=False, methods=['POST'], url_path='update_bankcard')
    def Set_bankcard(self, request):
        print(request.data)
        data = request.data
        arch_id = data.get("id")
        print(arch_id)
        user = ArchimatchUser.objects.get(id=arch_id)
        architect = Architect.objects.get(user=user)
        print(architect)
        if not architect.bankcard:
            bankcard = BankCard.objects.create(card_num=data.get('card_num'),card_holder=data.get('card_holder'),cvv=data.get('cvv'),expiration_date=data.get('expiration_date'))
            bankcard.save()
            architect.bankcard = bankcard
            architect.save()
            
            response_data = {
                'message': 'Architect Bankcard set successfully',
                'architect_id': architect.id
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
             architect.bankcard.card_num = data.get('card_num')
             architect.bankcard.card_holder = data.get('card_holder')
             architect.bankcard.cvv = data.get('cvv')
             architect.bankcard.expiration_date = data.get('expiration_date')
             architect.bankcard.save()
             response_data = {
                'message': 'Architect Bankcard updated successfully',
                'architect_id': architect.id
            }
             return Response(response_data, status=status.HTTP_200_OK)
## view ARCHITECT card by user id 
    @action(detail=False, methods=['GET'], url_path='find_archicard/(?P<arch_id>\d+)')
    def find_archicard(self, request,arch_id=None):
        
        architect = Architect.objects.get(user_id=arch_id)
        card = BankCard.objects.get(architect=architect)
        serializer = self.bankcard_serializer(card)
        response_data = {
                'message': 'Architect card found successfully'  ,
                'card': serializer.data          }
        return Response(response_data, status=status.HTTP_200_OK)
       


    ## Set Subscription to Architect
    @action(detail=False, methods=['POST'], url_path='set_subscription')
    def Set_subscription(self, request):
        print('aaaaaaaaa')
        print(request.data)
        data = request.data
        arch_id = data.get("id")
        print(arch_id)
        if Architect.objects.filter(user_id=arch_id).exists():
            architect = Architect.objects.get(user_id=arch_id)
            print(architect)
            sub_name = data.get('sub_name')
            print(sub_name)
            if sub_name:
                try:
                    sub = Subscription.objects.get(sub_name=sub_name)
                    print(sub)
                except Subscription.DoesNotExist:
                    return Response({"message": "Subscription with this name is not available"}, status=status.HTTP_400_BAD_REQUEST)          
                subscription = ArchiSubscription.objects.create(sub_name=sub.sub_name,free_tokens=sub.token_num,price=sub.price,active=True)
                subscription.save()
                architect.subscription = subscription
                Receipt.objects.create(architect=architect,email=architect.user.email,amount_paid=sub.price,sub_purchased=sub.sub_name,date_of_transaction=timezone.now())
                architect.save()
                sub = SubscriptionRequest.objects.get(id=data.get("req_id"))
                sub.delete()
                
                response_data = {
                    'message': 'Architect subscription enabled successfully',
                    'architect_id': architect.id
            }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                subscription_id = architect.subscription.id
                architect.subscription.delete()
                ArchiSubscription.objects.filter(id=subscription_id).delete()                
                architect.subscription = None
                architect.save()
                return Response({"message": "Architect subscription disabled successfully"}, status=status.HTTP_200_OK)

        



    ## Update Information des Preference 
    @action(detail=False, methods=['POST'], url_path='update_Preferences_info')
    def set_preferences_info(self, request):
        print(request.data)
        data = request.data
        arch_id = data.get("id")
        service = data.get("service", [])
        print(service)
        work_type = data.get("work_type", [])
        print(work_type)
        good_type = data.get("good_type", [])
        print(good_type)
        location = data.get("location", [])
        print(location)
        work_surface = data.get("work_surface", [])
        print(work_surface)
        project_budget = data.get("project_budget", [])
        print(project_budget)

        handled_service = ArchitectService.process_pref_services(service)
        handled_work_type = ArchitectService.process_pref_Worktypes(work_type)
        handled_good_type = ArchitectService.process_pref_goodtypes(good_type)
        handled_location = ArchitectService.process_pref_location(location)
        handled_work_surface = ArchitectService.process_pref_Worksurfaces(work_surface)
        handled_project_budget = ArchitectService.process_pref_Projectbudgets(project_budget)
        architect = Architect.objects.get(user_id=arch_id)
        print(architect)
        if (architect.preference):
            preference = architect.preference
            preference.service.set(handled_service)
            preference.work_type.set(handled_work_type)
            preference.good_type.set(handled_good_type)
            preference.location.set(handled_location)
            preference.work_surface.set(handled_work_surface)
            preference.project_budget.set(handled_project_budget)
            preference.save()
            response_message = 'Architect preferences updated successfully'

        else:
           preference = Preference.objects.create()
           preference.service.set(handled_service)
           preference.work_surface.set(handled_work_surface)
           preference.work_type.set(handled_work_type)
           preference.good_type.set(handled_good_type)
           preference.location.set(handled_location)
           preference.project_budget.set(handled_project_budget)
           architect.preference = preference
           architect.save()
           response_message = 'Architect preferences created successfully'
        response_data = {
            'message': response_message,
            'architect_id': architect.id
        }
        return Response(response_data, status=status.HTTP_200_OK)


    # update password Architect
    # update password Architect
    # update password Architect
    @action(detail=False, methods=['POST'], url_path='update_password_architect')
    def update_password(self, request):       
            print(request.data)
            data = request.data
            arch_id = data.get("id")
            actual_password = request.data.get("actual_password")
            architect = ArchimatchUser.objects.filter(id=arch_id).first()
            
            print(architect)
            if not check_password(actual_password,architect.password) :
                return Response({'error': 'Actual password is not correct'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                new_password = data.get('new_password')
                confirm_password = data.get('confirm_password')
                print(new_password)
                print(confirm_password)
                if new_password == confirm_password:
                    architect.set_password(new_password)
                    architect.save()
                    return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'New password and confirmation password do not match'}, status=status.HTTP_400_BAD_REQUEST)
    

   # View Factures by architect
    @action(detail=False, methods=['GET'], url_path='get_receipts/(?P<id>\d+)')
    def view_receipts(self, request, id=None):
        try:
            architect = Architect.objects.get(user_id=id)
        except Architect.DoesNotExist:
            return Response({"message": "Architect not found"}, status=status.HTTP_404_NOT_FOUND)
    
        receipts = Receipt.objects.filter(architect=architect)
        serializer = ReceiptSerializer(receipts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @action(detail=False, methods=['POST'], url_path='download_receipt_pdf')
    def download_receipt_pdf(self,request):
        data = request.data
        receipt_id = data.get('id')
        # Retrieve the receipt object
        try:
            # Retrieve the receipt object
            receipt = Receipt.objects.get(id=receipt_id)
        except Receipt.DoesNotExist:
            return JsonResponse({'error': 'Receipt not found'}, status=404)
        
        # Generate PDF response for the receipt
        pdf_file = ArchitectService.generate_receipt_pdf(receipt)
        return pdf_file
    
 ## view ARCHITECT PP
    @action(detail=False, methods=['GET'], url_path='View_pp/(?P<arch_id>\d+)')
    def find_architectpp(self, request, arch_id=None):
        try:
            architect = Architect.objects.get(user_id=arch_id)
        except Architect.DoesNotExist:
            return JsonResponse({'error': 'Architect not found'}, status=404)

        if architect.architect_avatar:  
            image_url = request.build_absolute_uri(architect.architect_avatar.url)
            print(image_url)
            return JsonResponse({'image_url': image_url})
        else:
            return JsonResponse({'error': 'Architect has no profile picture'})
    

    @action(detail=False, methods=['GET'], url_path='find_architect_by_user/(?P<arch_id>\d+)')
    def find_architect(self, request,arch_id=None):
        
        architect = Architect.objects.get(user_id=arch_id)
        serializer = self.serializer_class(architect)
        response_data = {
                'message': 'Architect found successfully'  ,
                'architect': serializer.data          }
        return Response(response_data, status=status.HTTP_200_OK)
    


    @action(detail=False, methods=['POST'], url_path='upload_video')
    def upload_video(self,request):
        arch_id = request.data.get('id')
        uploaded_file = request.FILES['video']
        # Retrieve the user and architect objects
        user = ArchimatchUser.objects.get(id=arch_id)
        architect = Architect.objects.filter(user=user).first()
        architect.video_presentation = uploaded_file
        architect.save()
        
        
        return Response({"message":"okay"},status=status.HTTP_200_OK)

        # archi rights
    @action(detail=False, methods=['GET'], url_path='get_rights/(?P<id>\d+)')
    def view_rights(self, request, id=None):

        service = ArchitectService()
        return service.Archi_rights(request,id=id)
    

    #Check Selected Project
    @action(detail=False, methods=['GET'], url_path='check_selection/(?P<announcement_id>\d+)/(?P<arch_id>\d+)')
    def Check_selected(self, request, announcement_id=None,arch_id=None):

        service = ArchitectService()
        return service.check_selection(request,announcement_id=announcement_id,arch_id=arch_id)
    
    #Fetch selection devis
    @action(detail=False, methods=['GET'], url_path='view_devis/(?P<announcement_id>\d+)/(?P<arch_id>\d+)')
    def view_selection_devis(self, request, announcement_id=None,arch_id=None):
        print(announcement_id)
        print(arch_id)
        service = ArchitectService()
        return service.View_announcement_devis(request,announcement_id=announcement_id,arch_id=arch_id)
    
    #Fetch devis details
    @action(detail=False, methods=['GET'], url_path='view_devis_details/(?P<id>\d+)')
    def view_devis_details(self, request, id=None):

        service = ArchitectService()
        return service.Devis_details(request,id=id)
    
    # Select a Project
    @action(detail=False, methods=['POST'], url_path='select_announcement')
    def select_announcement(self, request):

        service = ArchitectService()
        return service.annoucement_select(request)
    
        ## Update Profile picture 
    @action(detail=False, methods=['POST'], url_path='update_pdp')
    def architect_update_pdp(self, request):
        print(request.data)
        data = request.data
        arch_id = data.get("id")
        
        architect = Architect.objects.get(user_id=arch_id)
        architect.architect_avatar = request.FILES.get("architect_avatar")
        architect.save()

        response_data = {
             'message': 'Avatar updated successfully'            }
        return Response(response_data, status=status.HTTP_200_OK)
    
    # Create devis
    @action(detail=False, methods=['POST'], url_path='create_devis')
    def devis_create(self, request):

        service = ArchitectService()
        return service.devis_create(request)
    
    

    @action(detail=False, methods=['POST'], url_path='leave_project')
    def leave_project(self,request):
        
        data = request.data
        print("aaaaaaaaaaaaaaaaaaaaa",data)
        ann_id = data.get("ann_id")
        architect_id = data.get("architect_id")
        announcement = Announcement.objects.get(id=ann_id)
        architect = Architect.objects.get(user_id=architect_id)
        print(architect)
        selection = Selection.objects.get(announcement=announcement)
        selection.interested_architects.remove(architect)
        

        
        response_data = {
            'message': 'selected Announcements found',              
        }
                    
        return Response(response_data, status=status.HTTP_200_OK)    
    
    # # Display devis
    # @action(detail=False, methods=['GET'], url_path='view_devis_details/(?P<id>\d+)')
    # def display(self, request):

    #     service = ArchitectService()
    #     return service.devis_display(request)

    @action(detail=False, methods=['POST'], url_path='signaler_comment')
    def signaler_comment(self, request):

        
        data = request.data
        print(request.data)
        architect_id = data.get("architect_id")
        comment_id = data.get("comment_id")
        
        description = data.get("description")
        comment = Comment.objects.get(id=comment_id)
        user = ArchimatchUser.objects.get(id=architect_id)
        report = Report.objects.create(user=user,description=description)
        if CommentReport.objects.filter(comment=comment).exists():
            archiReport = CommentReport.objects.get(comment=comment)
        else :
            archiReport = CommentReport.objects.create(comment=comment)
        archiReport.rep_count= archiReport.rep_count+1
        archiReport.reports.add(report)
        archiReport.save()
        
        return Response({'message': 'you have added an architect'}, status=status.HTTP_200_OK)