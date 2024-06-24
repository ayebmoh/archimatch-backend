from rest_framework import viewsets
from archimatch_app.serializers.utils.SubscriptionSerializer import SubscriptionSerializer
from archimatch_app.models import Subscription
from archimatch_app.services import SubscriptionService
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class=SubscriptionSerializer
    queryset = Subscription.objects.all()

    def create(self, request):
        service = SubscriptionService()
        return service.Sub_create(request)
    
    
   

    @action(detail=False, methods=['POST'], url_path='update')
    def sub_update(self, request):
        print(request.data)
        data = request.data
        sub_id = data.get("id")

        name = data.get("sub_name")
        sub = Subscription.objects.get(id=sub_id)
        print(sub)

        
        
        if Subscription.objects.filter(sub_name=name).exclude(id=sub_id).exists():
            return Response({"message": "le nom du plan existe deja"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            sub.sub_name = data.get("sub_name")
            sub.token_num = data.get("token_num")
            sub.price = data.get("price")
            sub.prop_platform = data.get("prop_platform")
            sub.prop_profil = data.get("prop_profil")
            sub.realization_expo = data.get("realization_expo")
            sub.prop_selon_pref = data.get("prop_selon_pref")
            sub.mev_profil = data.get("mev_profil")
            sub.archi_supp = data.get("archi_supp")
            sub.fournisseur = data.get("fournisseur")
            sub.devi_gen = data.get("devi_gen")
            sub.active = data.get("active")
            sub.save()

            response_data = {
              'message': 'Subscription updated successfully',
              'sub_id': sub.id
           }
            return Response(response_data, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['GET'], url_path='find_archisub_by_user/(?P<arch_id>\d+)')
    def view_archisub(self,request, arch_id=None):

        service = SubscriptionService()
        return service.find_archisub(request,arch_id=arch_id)
    

    @action(detail=False, methods=['GET'], url_path='find_subscription_by_user/(?P<arch_id>\d+)')
    def view_oneSub(self,request, arch_id=None):

        service = SubscriptionService()
        return service.Show_Sub(request,arch_id=arch_id)