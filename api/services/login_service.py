from api.models import User, MenteeProfile, MentorProfile
from rest_framework.authtoken.models import Token
from api.serializers import UserSerializer, MentorProfileSerializer, MenteeProfileSerializer
import api.services.email_service as email_service
from django.conf import settings

def create_profile(user, user_type):
    if user_type == 'mentor':
        profile, created = MentorProfile.objects.get_or_create(user=user)
    else:
        profile, created = MenteeProfile.objects.get_or_create(user=user)
    return profile

def login_user(email, user_type, request_data):
    user, created = User.objects.get_or_create(username=email, email=email)
    if(not user.picture):
        if('picture' in request_data):
            user.picture = request_data['picture']
        if('first_name' in request_data):
            user.first_name = request_data['first_name']
        if('last_name' in request_data):
            user.last_name = request_data['last_name']
        user.save()
    Token.objects.get_or_create(user=user)
    if(created):
        email_service.send_email(user.email, settings.SENGRID_WELCOME_TEMPLATE_ID, {'name': user.first_name})
    return user

def login_with_validated_token(request_data, is_valid_token):
    is_valid, detail = is_valid_token(request_data)
    if(is_valid):
        email = request_data['email']
        user_type = request_data['user_type']
        user = login_user(email, user_type, request_data)
        profile = create_profile(user, user_type)
        user_serializer = UserSerializer(user)
        profile_serializer = MentorProfileSerializer(profile) if user_type == 'mentor' else MenteeProfileSerializer(profile)
        return {
            'authenticated': True,
            'user': user_serializer.data,
            'profile': profile_serializer.data,
            'user_type': user_type,
            'expires_in': detail
        }

    return {'authenticated': False, 'reason': detail}
