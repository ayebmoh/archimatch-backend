from rest_framework import viewsets
from ..serializers.RealizationSerializer import RealizationSerializer
from ..models import Realization
from archimatch_app.services import RealizationService
from rest_framework.decorators import action



class RealizationViewSet(viewsets.ModelViewSet):
    serializer_class=RealizationSerializer
    queryset = Realization.objects.all()
    
    @action(detail=False, methods=['post'], url_path='create_realization')
    def create_realization(self, request):
        service = RealizationService()
        return service.realization_create(request)
    
    @action(detail=False, methods=['post'], url_path='update_realization')
    def update_realization(self, request):
        service = RealizationService()
        return service.realization_update(request)
    
    @action(detail=False, methods=['post'], url_path='delete_realization')
    def delete_realization(self, request):
        service = RealizationService()
        return service.realization_delete(request)
    
    @action(detail=True, methods=['get'], url_path='view_realizations')
    def View_realizations(self, request,pk):
        service = RealizationService()
        return service.realizations_view(request,pk)


   
    @action(detail=True, methods=['get'], url_path='view_realization_by_id')
    def View_realization(self, request,pk):
        service = RealizationService()
        return service.realization_view(request,pk)
    

    @action(detail=False, methods=['get'], url_path='view_subCategories/(?P<category_name>[^/.]+)')
    def View_SubCategory(self, request, category_name=None):
        service = RealizationService()
        return service.View_SubCategories(category_name=category_name)
    
    @action(detail=False, methods=['get'], url_path='view_RealizationPerCategory/(?P<category_name>[^/.]+)')
    def View_RealPerCat(self, request, category_name=None):
        service = RealizationService()
        return service.View_RealizationPerCategory(category_name=category_name)


   