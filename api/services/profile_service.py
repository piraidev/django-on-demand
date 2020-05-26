from django.contrib.auth.models import User
from api.models import ConsumerProfile, SupplierProfile
from api.serializers import UserSerializer, SupplierProfileSerializer, ConsumerProfileSerializer
from django.conf import settings

def create_profile(user, user_type):
    if user_type == 'supplier':
        profile, created = SupplierProfile.objects.get_or_create(user=user)
    else:
        profile, created = ConsumerProfile.objects.get_or_create(user=user)
    return profile