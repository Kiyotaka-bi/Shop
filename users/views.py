from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.views import obtain_auth_token

from .models import ConfirmationCode
from .serializers import RegisterSerializer, ConfirmSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class ConfirmView(generics.GenericAPIView):
    serializer_class = ConfirmSerializer

    def post(self, request):

        username = request.data.get('username')
        code = request.data.get('code')

        try:
            user = User.objects.get(username=username)
            confirm_code = ConfirmationCode.objects.get(user=user)

            if confirm_code.code == code:
                user.is_active = True
                user.save()

                return Response({
                    "message": "Пользователь подтвержден"
                })

            return Response({
                "error": "Неверный код"
            }, status=400)

        except User.DoesNotExist:
            return Response({
                "error": "Пользователь не найден"
            }, status=404)
        except ConfirmationCode.DoesNotExist:
            return Response({
                "error": "Код подтверждения не найден"
            }, status=404)