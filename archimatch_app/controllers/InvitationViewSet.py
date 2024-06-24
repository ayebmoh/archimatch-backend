from rest_framework import viewsets
from ..serializers import ArchitectRequestSerializer,CommentSerializer,InvitationSerializer,InvitationAdminSerializer
from ..models import ArchitectRequest
from archimatch_app.models import Client,Architect,Comment,Invitation,ArchimatchUser
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


class InvitationViewSet(viewsets.ModelViewSet):
    serializer_class=InvitationSerializer
    queryset = Invitation.objects.all()
    
    
    

    def create(self,request):
        data = request.data
        email = data.get("email")
        architect_id = data.get("architect_id")

        architect = Architect.objects.get(user_id=architect_id)
        if ArchimatchUser.objects.filter(email=email).exists() or Invitation.objects.filter(invited_email=email).exists() :
            return Response({"message": "il y a un compte avec cet email"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            invitation = Invitation.objects.create(architect=architect,invited_email=email)        
            return Response({"message": "your invitation has been added"}, status=status.HTTP_201_CREATED)
    

    @action(detail=False, methods=['GET'], url_path='get_invitation_architect/(?P<id>\d+)')
    def get_invitation_architect(self, request, id=None):
        print(id)
        architect = Architect.objects.get(user_id=id)
        print(architect)
        invitations = Invitation.objects.filter(architect=architect)
        serializer = InvitationSerializer(invitations,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['GET'], url_path='get_invitation')
    def get_invitation(self, request, id=None):
        
        invitations = Invitation.objects.all()
        serializer = InvitationAdminSerializer(invitations,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'], url_path='handle_invitation')
    def handle_invitation(self, request, id=None):
        data = request.data
        print(data)
        action = request.data.get("action")
        id = request.data.get("id")
        invitations = Invitation.objects.get(id=id)
        if action:
            invitations.status = "Accepted"
        else :
            invitations.status = "Rejected"
        invitations.save()
        
        return Response({"message":"invitation handled"}, status=status.HTTP_200_OK)

