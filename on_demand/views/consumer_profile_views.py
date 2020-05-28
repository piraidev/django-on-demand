from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from on_demand.models import ConsumerProfile
from on_demand.serializers import ConsumerProfileSerializer


@api_view(['GET', 'PUT'])
def consumer_profile(request, user_id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        consumer_profile = ConsumerProfile.objects.get(user_id=user_id)
    except ConsumerProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        consumer_profile = ConsumerProfileSerializer(consumer_profile)
        return Response(consumer_profile.data)

    elif request.method == 'PUT':
        serializer = ConsumerProfileSerializer(
            consumer_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
