import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, viewsets
from django.contrib.auth import get_user_model

from ..account.serializers import UserSerializer


class HomeView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {
            'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(content)


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


# class GetAuthUser(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         return Response({'user': request.user})

class GetAuthUser(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = {
            'id': self.request.user.id,  # type: ignore
            'email': self.request.user.email,  # type: ignore
            'first_name': self.request.user.first_name, # type: ignore
            'last_name': self.request.user.last_name # type: ignore
        }
        return Response(user)
