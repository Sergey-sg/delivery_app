from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from rest_framework import status
from django.conf import settings

from .serializers import RegisterSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetAuthUser(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        photo = f'{self.request.user.photo}'  # type: ignore
        cloud_path = f"https://res.cloudinary.com/{settings.CLOUDINARY_STORAGE['CLOUD_NAME']}/image/upload/v1"
        if cloud_path not in photo:
            photo = f"{cloud_path}/{photo}"
        user = {
            'pk': self.request.user.pk,
            'email': self.request.user.email,  # type: ignore
            'first_name': self.request.user.first_name,  # type: ignore
            'last_name': self.request.user.last_name,  # type: ignore
            'address': self.request.user.address,  # type: ignore
            'img_alt': self.request.user.img_alt,  # type: ignore
            'phone_number': self.request.user.phone_number,  # type: ignore
            'photo': photo,
        }
        return Response(user)


class RegistrationViewSet(viewsets.ModelViewSet, TokenObtainPairView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "token": res["access"]
        }, status=status.HTTP_201_CREATED)
