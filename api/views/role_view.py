from rest_framework.decorators import api_view, permission_classes
from django.db import transaction
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import api.services.profile_service as profile_service
from api.serializers import UserSerializer, MentorProfileSerializer, MenteeProfileSerializer

@api_view(['POST'])
@transaction.atomic
@permission_classes((AllowAny, ))
def change_role(request):
    body = request.data
    user_id = body['user_id']
    user_type = body['user_type']

    user = User.objects.get(id=user_id)
    profile = profile_service.create_profile(user, user_type)
    if (user_type == 'mentor'):
        serializer = MentorProfileSerializer(profile)
    else:
        serializer = MenteeProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)
