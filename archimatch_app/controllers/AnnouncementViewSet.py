from rest_framework import viewsets
from archimatch_app.serializers import AnnouncementSerializer
from archimatch_app.models import Announcement,Client
from archimatch_app.services import AnnouncementService
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class=AnnouncementSerializer
    queryset = Announcement.objects.all()

    def create(self, request):
        service = AnnouncementService()
        return service.annoucement_create(request)
    
    @action(detail=False, methods=['POST'], url_path='loggedIn')
    def announcement_create_logged_in(self, request):       
        service = AnnouncementService()
        return service.annoucement_create_logged_in(request)
    

    @action(detail=False, methods=['GET'], url_path='get_announcements_by_client/(?P<arch_id>\d+)')
    def get_announcements_by_client(self, request,arch_id=None):
        
        client = Client.objects.get(user_id=arch_id)
        announcements = Announcement.objects.filter(client=client)
        serializer = self.serializer_class(announcements,many=True)
        response_data = {
                'message': 'announcements found successfully'  ,
                'announcements': serializer.data          }
        return Response(response_data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'], url_path='delete_announcement')
    def delete_announcement(self, request,arch_id=None):
        
        announcement = Announcement.objects.get(id=request.data.get("id"))
        announcement.delete()
        response_data = {
                'message': 'announcement deleted '  ,
                    }
        return Response(response_data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'], url_path='change_found_status')
    def change_found_status(self, request):
        
        announcement = Announcement.objects.get(id=request.data.get("id"))
        if announcement.architect_found : 
            announcement.architect_found = False
        else :
            announcement.architect_found = True
        
        announcement.save()
        response_data = {
                'message': 'announcement changed '  ,
                    }
        return Response(response_data, status=status.HTTP_200_OK)