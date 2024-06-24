from rest_framework import viewsets
from ..serializers import SelectionSerializer
from ..models import Selection
from archimatch_app.models import ArchitectType
from rest_framework.response import Response
from rest_framework import status
from archimatch_app.services import SelectionService
from rest_framework.decorators import action



class SelectionViewSet(viewsets.ModelViewSet):
    serializer_class=SelectionSerializer
    queryset = Selection.objects.all()


    @action(detail=False, methods=['GET'], url_path='get_not_selected_announcements/(?P<id>\d+)')
    def view_not_selected_announcements(self, request, id=None):
        service = SelectionService()
        return service.view_not_selected_announcements(id)
    
    @action(detail=False, methods=['GET'], url_path='get_selections/(?P<id>\d+)')
    def view_selections(self, request, id=None):
        service = SelectionService()
        return service.view_selected_announcements(id)
    
    @action(detail=False, methods=['GET'], url_path='get_selections_by_announcement/(?P<id>\d+)')
    def get_selections_by_announcement(self, request, id=None):
        service = SelectionService()
        return service.get_selections_by_announcement(id)
    
    @action(detail=False, methods=['POST'], url_path='create_devis')
    def create_devis(self, request, id=None):
        service = SelectionService()
        return service.create_devis(request)

    