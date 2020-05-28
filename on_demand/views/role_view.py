from rest_framework.decorators import api_view, permission_classes
from django.db import transaction
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import on_demand.services.profile_service as profile_service
from on_demand.serializers import UserSerializer, SupplierProfileSerializer, ConsumerProfileSerializer


@api_view(['POST'])
@transaction.atomic
@permission_classes((AllowAny, ))
def change_role(request):
    body = request.data
    user_id = body['user_id']
    user_type = body['user_type']

    user = User.objects.get(id=user_id)
    profile = profile_service.create_profile(user, user_type)
    if (user_type == 'supplier'):
        serializer = SupplierProfileSerializer(profile)
    else:
        serializer = ConsumerProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)
