from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from django.contrib.auth import get_user_model


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        if self.request.user.is_superuser:  # type: ignore
            return get_user_model().objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = get_user_model().objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj
