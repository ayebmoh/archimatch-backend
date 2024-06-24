from archimatch_app.models import ArchitectType,NeedPieces,Announcement,Client
from archimatch_app.models import ArchitectRequest,ArchimatchUser
from archimatch_app.serializers import AnnouncementSerializer
from rest_framework.response import Response
from rest_framework import status
from django.template.loader import render_to_string
from archimatch_app.services.utils import send_email_with_template
from archimatch_project import settings
from django.db import transaction
from django.db.utils import IntegrityError

class AnnouncementService:
    serializer_class = AnnouncementSerializer
    
    def architect_type_process(self,architect_type,data):
        
        filtered_instances = ArchitectType.objects.filter(display=architect_type)
        
        instance = None
        if not filtered_instances.exists():

            print("bbbbbbbb")
            instance = ArchitectType.objects.create(display=architect_type)
            data["architect_type"]= instance.id
           
        else:
            instance = filtered_instances.first()
            print(instance)
            data["architect_type"]= instance.id
        
        
    def annoucement_create(self, request):
        data = request.data
        print(request.data)
        user_data = data.pop("user", None)
        images = data.pop('images', None)
        need_pieces_data = data.pop("needed_pieces", None)
        
        # Check if the user exists
        if ArchimatchUser.objects.filter(email=user_data.get("email")).exists():
            return Response({"message": "email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Create or get ArchitectType instance
        architect_type_instance, _ = ArchitectType.objects.get_or_create(display=data["architect_type"])

        # Create NeedPieces instance
        data.pop("architect_type",None)
        new_need_pieces = NeedPieces.objects.create(**need_pieces_data)

        # Create or get Client instance and associate it with ArchimatchUser
        user_data["user_type"] = "Client"
        client_user = ArchimatchUser.objects.create(**user_data)
        client_instance, _ = Client.objects.get_or_create(user=client_user)

        # Create Announcement instance and assign related instances
        new_announcement = Announcement.objects.create(
            architect_type=architect_type_instance,
            need_pieces=new_need_pieces,
            client=client_instance,
            **data
        )


        reset_link = f"http://localhost:3000/clientVisitor/CreatePassword/{client_user.id}"  
        html_content = render_to_string(template_name="reset_password.html", context={'reset_link': reset_link})
        send_email_with_template(
            user_data.get("email"),
            "Reset Password",
            html_content,
            settings.COMMON_IMAGES
        )

        response_data = {
            'message': 'Object created successfully with custom status code',
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    


    def annoucement_create_logged_in(self, request):
        data = request.data
        print(request.data)

        images = data.pop('images', None)
        need_pieces_data = data.pop("needed_pieces", None)

        try:
            with transaction.atomic():
                # Create or get ArchitectType instance
                architect_type_instance, _ = ArchitectType.objects.get_or_create(display=data["architect_type"])

                # Create NeedPieces instance
                data.pop("architect_type",None)
                new_need_pieces = NeedPieces.objects.create(**need_pieces_data)

                # Create or get Client instance and associate it with ArchimatchUser
                client_instance = Client.objects.get(id=request.data.get("id"))


                # Ensure the 'id' field is not included in 'data'
                if 'id' in data:
                    del data['id']
                # Create Announcement instance and assign related instances
                new_announcement = Announcement.objects.create(
                    architect_type=architect_type_instance,
                    need_pieces=new_need_pieces,
                    client=client_instance,
                    **data
                )
                print("aaaaaaa")

            response_data = {
                'message': 'Object created successfully with custom status code',
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({'error': 'Integrity error occurred: {}'.format(str(e))}, status=status.HTTP_400_BAD_REQUEST)
        except Client.DoesNotExist:
            return Response({'message': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'An error occurred: {}'.format(str(e))}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)