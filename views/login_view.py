from rest_framework.decorators import api_view, permission_classes
from django.db import transaction
from models.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import services.login_service as login_service
from serializers.serializers import UserSerializer, MentorProfileSerializer, MenteeProfileSerializer
import services.linkedin_helper as lh
import services.facebook_helper as fh
import services.google_helper as gh

@api_view(['POST'])
@transaction.atomic
@permission_classes((AllowAny, ))
def fb_login(request):
    body = request.data
    request_data = {
        'auth_service': 'facebook',
        'email': body['email'],
        'first_name': body['first_name'],
        'last_name': body['last_name'],
        'token': body['token'],
        'user_id': body['user_id'],
        'user_type': body['user_type'],
        'picture': body['picture']
        }

    response = login_service.login_with_validated_token(request_data, fh.is_valid_token)
    return Response(response)

@api_view(['POST'])
@transaction.atomic
@permission_classes((AllowAny, ))
def linkedin_login(request):
    body = request.data
    username = body['username']
    user_type = body['user_type']
    authorization_code = body['authorization_code']
    access_token, detail = lh.get_access_token(authorization_code)

    if(access_token):
        user = login_service.login_user(username, )
        user_serializer = UserSerializer(user)
        return Response({'authenticated': True, 'user': user_serializer.data, 'expires_in': detail})
    
    return Response({'authenticated': False, 'reason': detail})

@api_view(['POST'])
@transaction.atomic
@permission_classes((AllowAny, ))
def google_login(request):
    body = request.data
    request_data = {
        'auth_service': 'google',
        'email': body['email'],
        'first_name': body['first_name'],
        'last_name': body['last_name'],
        'user_type': body['user_type'],
        'token': body['token'],
        'user_id': body['user_id'],
        'picture': body['picture']
    }

    response = login_service.login_with_validated_token(request_data, gh.is_valid_token)
    return Response(response)

@api_view(['POST'])
@transaction.atomic
@permission_classes((AllowAny, ))
def change_role(request):
    body = request.data
    user_id = body['user_id']
    user_type = body['user_type']

    user = User.objects.get(id=user_id)
    profile = login_service.create_profile(user, user_type)
    if (user_type == 'mentor'):
        serializer = MentorProfileSerializer(profile)
    else:
        serializer = MenteeProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)
