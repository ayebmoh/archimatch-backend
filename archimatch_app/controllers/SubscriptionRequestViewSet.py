from rest_framework import viewsets
from ..serializers import SubscriptionRequestSerializer
from ..models import SubscriptionRequest
from archimatch_app.services import SubscriptionRequestService
from django.contrib.auth.hashers import make_password
from archimatch_app.services.utils import send_email_with_template
from archimatch_project import settings
from django.template.loader import render_to_string


class SubscriptionRequestViewSet(viewsets.ModelViewSet):
    serializer_class=SubscriptionRequestSerializer
    queryset = SubscriptionRequest.objects.all()
    
    def create(self, request):
        service = SubscriptionRequestService()
        return service.Subrequest_create(request)
    

   
