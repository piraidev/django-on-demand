from django.contrib.auth.models import User
from on_demand.models import ConsumerProfile, SupplierProfile
from on_demand.serializers import UserSerializer, SupplierProfileSerializer, ConsumerProfileSerializer


def create_profile(user, user_type):
    if user_type == 'supplier':
        profile, created = SupplierProfile.objects.get_or_create(user=user)
    else:
        profile, created = ConsumerProfile.objects.get_or_create(user=user)
    return profile
