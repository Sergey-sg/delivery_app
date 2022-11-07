from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.conf import settings


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
