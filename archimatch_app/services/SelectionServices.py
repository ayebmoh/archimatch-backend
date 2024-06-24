from archimatch_app.serializers import SelectionSerializer,AnnouncementSerializer
from rest_framework.response import Response
from rest_framework import status
from archimatch_app.models import Architect,Selection,Announcement,Devis
from django.contrib.auth.hashers import make_password


class SelectionService:
    serializer_class = SelectionSerializer
    announcement_serializer = AnnouncementSerializer
    

    def view_not_selected_announcements(self,id=None):
        print("id is",id)
        architect = Architect.objects.get(user_id=id)
        print(architect)
        selected_announcement_ids = Selection.objects.filter(interested_architects=architect).values_list('announcement_id', flat=True)
        not_selected_announcements = Announcement.objects.exclude(id__in=selected_announcement_ids)
        if not_selected_announcements:
            serializer = self.announcement_serializer(not_selected_announcements,many=True)
            response_data = {
                    'message': 'Announcements that not selected found',
                    'Announcements': serializer.data
                }
        
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                    'message': 'All announcements are selected',
                    'Announcements': None
                }
            return Response(response_data, status=status.HTTP_200_OK)

            
            

    def view_selected_announcements(self,id=None):
        print("id is",id)
        architect = Architect.objects.get(user_id=id)
        print(architect)
        selections = Selection.objects.all()
        selected_announcement = []
        for selection in selections : 
            if selection.interested_architects.filter(id = architect.id).exists():
                selected_announcement.append(selection.announcement)
        
        serializer = self.announcement_serializer(selected_announcement,many=True)
        response_data = {
                'message': 'selected Announcements found',
                'Selections': serializer.data
            }
        
        return Response(response_data, status=status.HTTP_200_OK)
        
    

    def get_selections_by_announcement(self,id=None):
        print("id is",id)
        announcement = Announcement.objects.get(id=id)
       
        selected_announcements = Selection.objects.filter(announcement=announcement)
        if selected_announcements :
            selection = Selection.objects.get(announcement=announcement)
            serializer = self.serializer_class(selection)
            response_data = {
                        'message': 'selected Announcements found',
                        'Selections': serializer.data
                }
        
        else :
            response_data = {
                            'message': 'selected Announcements found',
                            'Selections': {}
                    }
        return Response(response_data, status=status.HTTP_200_OK)

    def create_devis(self,request):
        
        data = request.data
        print("aaaaaaaaaaaaaaaaaaaaa",data)
        ann_id = data.get("ann_id")
        architect_id = data.get("architect_id")
        announcement = Announcement.objects.get(id=ann_id)
        architect = Architect.objects.get(user_id=architect_id)
        selection = Selection.objects.get(announcement=announcement)
        new_devis = Devis.objects.create(architect=architect, status="Pending", file=request.FILES.get("devis"))
        selection.devis.add(new_devis)
        
        response_data = {
            'message': 'selected Announcements found',              
        }
                    
        return Response(response_data, status=status.HTTP_200_OK)
        