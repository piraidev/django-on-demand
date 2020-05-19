from api.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from api.serializers import UserSerializerWithoutAuthData
from django_filters.rest_framework import DjangoFilterBackend
import api.services.email_service as email_service

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializerWithoutAuthData
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['id']

    #Adding this function as an example of a custom action for the view set
    @action(detail=False)
    def get_first(self, request):
        first_user = User.objects.first()
        user_serializer = UserSerializerWithoutAuthData(first_user)
        return Response(user_serializer.data)

    @action(detail=True, methods=['post'])
    def unsubscribe(self, request, pk=None):
        user = self.get_object()
        try:
            email_service.unsubscribe_user(user.email)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response('error', status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def subscribe(self, request, pk=None):
        user = self.get_object()
        try:
            email_service.subscribe_user(user.email)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response('error', status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def is_subscribed(self, request, pk=None):
        user = self.get_object()
        try:
            is_subscribed = email_service.user_is_subscribed(user.email)
            return Response({'is_subscribed':is_subscribed}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response('error', status=status.HTTP_400_BAD_REQUEST)