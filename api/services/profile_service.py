from django.contrib.auth.models import User
from api.models import MenteeProfile, MentorProfile
from api.serializers import UserSerializer, MentorProfileSerializer, MenteeProfileSerializer
from django.conf import settings

def create_profile(user, user_type):
    if user_type == 'mentor':
        profile, created = MentorProfile.objects.get_or_create(user=user)
    else:
        profile, created = MenteeProfile.objects.get_or_create(user=user)
    return profile