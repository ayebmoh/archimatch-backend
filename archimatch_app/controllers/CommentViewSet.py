from rest_framework import viewsets
from ..serializers import ArchitectRequestSerializer,CommentSerializer
from ..models import ArchitectRequest
from archimatch_app.models import Client,Architect,Comment
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


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class=CommentSerializer
    queryset = ArchitectRequest.objects.all()
    
    
    

    def create(self,request):
        data = request.data
        client_id = data.get("client_id")
        architect_id = data.get("architect_id")

        architect = Architect.objects.get(id=architect_id)
        client = Client.objects.get(user_id=client_id)
        comment = Comment.objects.create(architect=architect, Client=client, message=data.get('message'))
       
        

        return Response({"message": "your comment has been added"}, status=status.HTTP_201_CREATED)

