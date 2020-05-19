from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import MenteeProfile
from api.serializers import MenteeProfileSerializer

@api_view(['GET', 'PUT'])
def mentee_profile(request, user_id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        mentee_profile = MenteeProfile.objects.get(user_id=user_id)
    except MenteeProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        mentee_profile = MenteeProfileSerializer(mentee_profile)
        return Response(mentee_profile.data)

    elif request.method == 'PUT':
        serializer = MenteeProfileSerializer(mentee_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
