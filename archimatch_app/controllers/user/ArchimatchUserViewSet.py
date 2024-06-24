from rest_framework import viewsets
from archimatch_app.serializers import ArchiMatchUserSerializer,ArchiMatchUserTokenSerializer
from archimatch_app.models import ArchimatchUser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.core.exceptions import ObjectDoesNotExist
from archimatch_app.serializers.ResetPasswordSerializer import PasswordResetSerializer
from archimatch_app.serializers.ConfirmPasswordSerializer import PasswordConfirmSerializer
from django.template.loader import render_to_string
from archimatch_app.services.utils import send_email_with_template
from archimatch_project import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from rest_framework.decorators import action


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = dict()
        serializer = ArchiMatchUserTokenSerializer(self.user).data
        for key,value in serializer.items():
            if key !="token":
                user[key] = value
            else :
                data[key]=value
        data["user"] = user
        return data
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['user'] = ArchiMatchUserSerializer(user).data
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            # html_content = render_to_string(template_name="welcome_email.html", context={})
            # send_email_with_template(
            #     "ghazichaftar@gmail.com", "topic1", html_content, settings.COMMON_IMAGES
            # )
        except AuthenticationFailed as e:
            try:
                found_user = ArchimatchUser.objects.get(username = request.data.get("username"))
                print(found_user)
                return Response({"message":"mot de passe incorrecte"}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"message":"email n'existe pas"}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


    



class PasswordResetView(APIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data.get("email")
            user = ArchimatchUser.objects.filter(username=email).first()
            print(user.username)
            if not user:
                return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
            uidb64 = user.pk
            print(uidb64)
            reset_link = f"http://localhost:3000/archVisitor/CreateNewPassword/{uidb64}"  
            html_content = render_to_string(template_name="reset_password.html", context={'reset_link': reset_link})

            send_email_with_template(
                email,
                "Reset Password",
                html_content,
                settings.COMMON_IMAGES
            )

            return Response({'message': 'Password reset email sent successfully.'}, status=status.HTTP_200_OK)
        
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PasswordConfirmView(APIView):
    serializer_class = PasswordConfirmSerializer

    def post(self, request, *args, **kwargs):
        
        try:
            print(request.data)
            uid = request.data.get("id")
            user = get_user_model().objects.get(pk=uid)
            print(user)
        except (TypeError, ValueError, OverflowError, ObjectDoesNotExist):
            user = None
        if not user :
            return Response({'error': 'Invalid UID'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(data=request.data, context={'user': user})
        if serializer.is_valid():
            new_password = serializer.validated_data.get('new_password')
            confirm_password = serializer.validated_data.get('confirm_password')
            print(new_password)
        
            print(confirm_password)
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'New password and confirmation password do not match'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

           

class ArchimatchUserViewSet(viewsets.ModelViewSet):
    serializer_class=ArchiMatchUserSerializer
    queryset = ArchimatchUser.objects.all()

    @action(detail=True, methods=['GET'], url_path='by_id')
    def get_user_by_id(self,request,pk):
        uid = pk
        queryset = ArchimatchUser.objects.get(id=uid)
        serializer = ArchiMatchUserSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    