from archimatch_app.serializers import DevisSerializer,ArchitectSerializer,SubscriptionSerializer,SelectionSerializer
from rest_framework.response import Response
from rest_framework import status
from archimatch_app.models import Devis,Selection,Announcement,ArchiServicetype,Services,Worksurface,Worktype,Goodtype,Projectbudget,Location,Receipt,Architect,Subscription
from django.contrib.auth.hashers import make_password
from io import BytesIO
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import pdfkit
from django.template.loader import render_to_string

class ArchitectService:
    serializer_class = ArchitectSerializer
    subscription_class = SubscriptionSerializer
    selection_class = SelectionSerializer
    Devis_class = DevisSerializer


    @classmethod
    def process_pref_services(self, services):
        handled_pref_services = []
        for service in services:
            existing_service = Services.objects.filter(display=service).first()  # Get first existing service
            if existing_service:
                handled_pref_services.append(existing_service.id)
            else:
                new_service = Services.objects.create(display=service)
                handled_pref_services.append(new_service.id)
        return handled_pref_services
  
    @classmethod
    def process_pref_location(self, locations):
        handled_locations = []
        for location in locations:
            existing_location = Location.objects.filter(display=location).first()  # Get first existing service
            if existing_location:
                handled_locations.append(existing_location.id)
            else:
                new_location = Location.objects.create(display=location)
                handled_locations.append(new_location.id)
        return handled_locations
   
   
    @classmethod
    def process_pref_goodtypes(self, Goodtypes):
        handled_goodtypes = []
        for goodtype in Goodtypes:
            existing_Goodtype = Goodtype.objects.filter(display=goodtype).first()  # Get first existing service
            if existing_Goodtype:
                handled_goodtypes.append(existing_Goodtype.id)
            else:
                new_goodtype = Goodtype.objects.create(display=goodtype)
                handled_goodtypes.append(new_goodtype.id)
        return handled_goodtypes
   
    @classmethod
    def process_pref_Worktypes(self, Worktypes):
        handled_Worktypes = []
        for worktype in Worktypes:
            existing_Worktype = Worktype.objects.filter(display=worktype).first()
            if existing_Worktype:
                handled_Worktypes.append(existing_Worktype.id)
            else:
                new_worktype = Worktype.objects.create(display=worktype)
                handled_Worktypes.append(new_worktype.id)
        return handled_Worktypes
   
    @classmethod
    def process_pref_Projectbudgets(self, Projectbudgets):
        handled_projectbudget = []
        for projectbudget in Projectbudgets:
            existing_projectbudget = Projectbudget.objects.filter(display=projectbudget).first()  # Get first existing service
            if existing_projectbudget:
                handled_projectbudget.append(existing_projectbudget.id)
            else:
                new_projectbudget = Projectbudget.objects.create(display=projectbudget)
                handled_projectbudget.append(new_projectbudget.id)
        return handled_projectbudget
    
    @classmethod
    def process_pref_Worksurfaces(self, Worksurfaces):
        handled_Worksurfaces = []
        for worksurface in Worksurfaces:
            existing_worksurface = Worksurface.objects.filter(display=worksurface).first()
            if existing_worksurface:
                handled_Worksurfaces.append(existing_worksurface.id)
            else:
                new_worksurface = Worksurface.objects.create(display=worksurface)
                handled_Worksurfaces.append(new_worksurface.id)
        return handled_Worksurfaces


    @classmethod
    def process_services(self, services):
        handled_services = []
        for service in services:
            existing_service = ArchiServicetype.objects.filter(display=service).first()  # Get first existing service
            if existing_service:
                handled_services.append(existing_service.id)
            else:
                new_service = ArchiServicetype.objects.create(display=service)
                handled_services.append(new_service.id)
        return handled_services

    def architect_get_by_email(self,request,pk):
        data = request.data
        print(pk)
        print("email")
        response_data = {
            'message': 'email',
            
        }
        return Response(response_data, status=status.HTTP_200_OK)


    @classmethod
    def generate_receipt_pdf(self,receipt):

    # Render the HTML template with the receipt data
     html_content = render_to_string('receipt.html', {'receipt': receipt})


     config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

    # Convert HTML to PDF
     pdf = pdfkit.from_string(html_content, False, configuration=config)
    # Prepare HTTP response with PDF content
     response = HttpResponse(pdf, content_type='application/pdf')
     response['Content-Disposition'] = f'attachment; filename="receipt_{receipt.id}.pdf"'
     return response
        
    # Architects rights checker
    def Archi_rights(self,request,id=None):
       
        try:
            architect = Architect.objects.get(user_id=id)
            print (architect)
            sub_name = architect.subscription.sub_name
            subscription = Subscription.objects.get(sub_name=sub_name)

            serializer = self.subscription_class(subscription)
            response_data = {
            'message': 'Objects found successfully',
            'realization': serializer.data
        }
            return Response(response_data, status=status.HTTP_200_OK)
        except Architect.DoesNotExist:
            return Response({"message": "Architect not found"}, status=status.HTTP_404_NOT_FOUND)
        


    def annoucement_select(self, request):
        data = request.data
        print(data)
        arch_id = data.get("arch_id")
        anouncement_id = data.get("announcement_id")
        architect = Architect.objects.get(user_id=arch_id)
        print(architect)
        announcement = Announcement.objects.get(id=anouncement_id)
        print(announcement)
        if Selection.objects.filter(announcement=announcement).exists():
            selection = Selection.objects.get(announcement=announcement)
        else :
            selection = Selection.objects.create(announcement=announcement)
        selection.interested_architects.add(architect)
        announcement.selection_count = announcement.selection_count + 1
        announcement.save()
        
        subscription = architect.subscription
        if architect.tokens < 5 :
            return Response({"message":"Vous n'avez pas de jetons pour selectionner ce projet"}, status=status.HTTP_400_BAD_REQUEST)
        architect.tokens -= 5
        architect.save()
        # architect.subscription.tokens 
        # remove the amount of tokens from the archi 
        serializer = self.selection_class(selection)
        response_data = {
            'message': 'Objects created successfully',
            'Selection': serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    


    def check_selection(self, request, arch_id=None, announcement_id=None):
        try:
            architect = Architect.objects.get(user_id=arch_id)
            announcement = Announcement.objects.get(id=announcement_id)
            selection = Selection.objects.filter(announcement=announcement).first()
            
            if selection and selection.interested_architects.filter(id=architect.id).exists():
                serializer = self.selection_class(selection)
                response_data = {
                    'message': 'Selection found successfully',
                    'selection': serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data = {
                    'message': 'Selection not found',
                    'selection': None
                }
                return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        except Architect.DoesNotExist:
            return Response({'message': 'Architect not found'}, status=status.HTTP_404_NOT_FOUND)
        except Announcement.DoesNotExist:
            return Response({'message': 'Announcement not found'}, status=status.HTTP_404_NOT_FOUND)

        


    def View_announcement_devis(self, request, arch_id=None, announcement_id=None):
        try:
            print("aaaaaaaaaaaaaaaaa")
            architect = Architect.objects.get(user_id=arch_id)
            announcement = Announcement.objects.get(id=announcement_id)
            selection = Selection.objects.filter(announcement=announcement).first()
            devis = selection.devis.all()  # Accessing all related Devis objects
            if devis:
                serializer = self.Devis_class(devis,many=True)
                response_data = {
                    'message': 'devis found successfully',
                    'devis': serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data = {
                    'message': 'devis not found',
                    'devis': None
                }
                return Response(response_data, status=status.HTTP_200_OK)
        except Architect.DoesNotExist:
            return Response({'message': 'Architect not found'}, status=status.HTTP_404_NOT_FOUND)
        except Announcement.DoesNotExist:
            return Response({'message': 'Announcement not found'}, status=status.HTTP_404_NOT_FOUND)
       

    def Devis_details(self,request,id=None):
       
        try:
            devis = Devis.objects.get(id=id)
            print (devis)

            serializer = self.Devis_class(devis)
            response_data = {
            'message': 'devis details found successfully',
            'devis': serializer.data
        }
                 
            return Response(response_data, status=status.HTTP_200_OK)
        except Devis.DoesNotExist:
            return Response({"message": "Devis not found"}, status=status.HTTP_404_NOT_FOUND)
        

    def devis_create(self,request):
        data = request.data
        selection_id = data.get('id')
        pdf = request.FILES.get('pdf')
        if not pdf.name.endswith('.pdf'):
            return JsonResponse({'error': 'File must be a PDF'}, status=400)
        try:
            # Retrieve the receipt object
            selection = Selection.objects.get(id=selection_id)
        except Receipt.DoesNotExist:
            return JsonResponse({'error': 'Selection not found'}, status=404)
        devis = Devis.objects.create(file=pdf)
        selection.devis.add(devis)
        selection.save()
        
        # Generate PDF response for the receipt
        return JsonResponse({'message':'Devis added successfuly'},status=200)
    




    def devis_display(self,id=None):
        try:
            devis = Devis.objects.get(id=id)
        except Receipt.DoesNotExist:
            return JsonResponse({'error': 'Devis not found'}, status=404)
        
        pdf_file = devis.file()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{pdf_file.name}"'
        return response
