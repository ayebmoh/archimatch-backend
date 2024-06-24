from archimatch_app.serializers.utils import SubscriptionSerializer
from archimatch_app.serializers import ArchiSubscriptionSerializer
from rest_framework.response import Response
from rest_framework import status
from archimatch_app.models import Architect,ArchiSubscription
from archimatch_app.models import Subscription
from rest_framework.decorators import action


class SubscriptionService:
    serializer_class = SubscriptionSerializer
    sub_class = ArchiSubscriptionSerializer


    def Sub_create(self,request):
        data = request.data
        sub_name = data.get('sub_name')
       

        if Subscription.objects.filter(sub_name=sub_name).exists():
            return Response({"message": "le Plan d'abonnement avec ce nom existe deja"}, status=status.HTTP_400_BAD_REQUEST)
        
        new_sub = Subscription.objects.create(**data)

        response_data = {
            'message': 'Object created successfully with custom status code',
            'sub_id': new_sub.id,
            'sub_name': new_sub.sub_name
            
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


    # Find Architect subscription informations
    def find_archisub(self,request,arch_id=None):
        architect = Architect.objects.get(user_id=arch_id)
        subscription = architect.subscription
        serializer = self.sub_class(subscription)
        response_data = {
                'message': 'Architect Subscription found successfully'  ,
                'Archisub': serializer.data          }
        return Response(response_data, status=status.HTTP_200_OK)
   
    # show Architect subscription informations
    def Show_Sub(self,request,arch_id=None):
        architect = Architect.objects.get(user_id=arch_id)
        sub_name = architect.subscription.sub_name
        subscription = Subscription.objects.get(sub_name=sub_name)
        serializer = self.serializer_class(subscription)
        response_data = {
                'message': 'Subscription found successfully'  ,
                'subscription': serializer.data          }
        return Response(response_data, status=status.HTTP_200_OK)