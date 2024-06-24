from archimatch_app.serializers.SubscriptionRequest import SubscriptionRequestSerializer
from rest_framework.response import Response
from rest_framework import status
from archimatch_app.models.utils.SubscriptionRequest import SubscriptionRequest
from archimatch_app.models import Architect,Subscription,ArchiSubscription

class SubscriptionRequestService:
    serializer_class = SubscriptionRequestSerializer



    def Subrequest_create(self,request):
        data = request.data
        email = data.get('email')
        print(data)

        if SubscriptionRequest.objects.filter(email=email).exists():
            return Response({"message": "La demande d'abonnement avec cet email exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        new_sub = SubscriptionRequest.objects.create(**data)
        free_sub = Subscription.objects.filter(price=0).first()
        print(free_sub)
        architect = Architect.objects.get(user__email=email)
        print(architect)
        new_archisub = ArchiSubscription.objects.create(sub_name=free_sub.sub_name, free_tokens=free_sub.token_num,price=free_sub.price,active=True)
        print(new_sub)
        architect.subscription = new_archisub
        architect.save()
        
        response_data = {
            'message': 'Object created successfully with custom status code',
            'sub_id': new_sub.id,
            'sub_name': new_sub.email
            
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

   