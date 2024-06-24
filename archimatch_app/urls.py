from django.urls import path, include
from rest_framework import routers
from .controllers import SelectionViewSet,RealizationViewSet,SubscriptionRequestViewSet,SubscriptionViewSet,PasswordConfirmView,PasswordResetView,AnnouncementViewSet,ArchitectRequestViewSet,MyTokenObtainPairView,ArchimatchUserViewSet,AdminViewSet,ArchitectViewSet,CommentViewSet,InvitationViewSet,SupplierViewSet
from .controllers.user.ClientViewSet import ClientPasswordResetView,ClientPasswordConfirmView,ClientViewSet

from rest_framework_simplejwt.views import (
    TokenRefreshView
)

   

router = routers.DefaultRouter()
router.register('announcement', AnnouncementViewSet)
router.register('architectRequest',ArchitectRequestViewSet)
router.register('admin',AdminViewSet)
router.register("user",ArchimatchUserViewSet)
router.register("architect",ArchitectViewSet)
router.register("client",ClientViewSet)
router.register('subscriptions', SubscriptionViewSet)
router.register('subscriptionrequest', SubscriptionRequestViewSet)
router.register('Realization', RealizationViewSet)
router.register('Selection', SelectionViewSet)
router.register('Comment', CommentViewSet)
router.register('Invitation', InvitationViewSet)
router.register('supplier',SupplierViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('reset_password_architect/', PasswordResetView.as_view(), name='password_reset_architect'),
   path('confirm_reset_password_architect/', PasswordConfirmView.as_view(), name='password_confirm_architect'),
   path('password_reset_client/', ClientPasswordResetView.as_view(), name='reset-password-client'),
   path('confirm_password_reset-client/', ClientPasswordConfirmView.as_view(), name='confirm_password_client'),
   

]     