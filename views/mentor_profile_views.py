from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models.models import MentorProfile
from serializers.serializers import MentorProfileSerializer

@api_view(['GET', 'PUT'])
def mentor_profile(request, user_id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        mentor_profile = MentorProfile.objects.get(user_id=user_id)
    except MentorProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        mentor_profile = MentorProfileSerializer(mentor_profile)
        return Response(mentor_profile.data)

    elif request.method == 'PUT':
        serializer = MentorProfileSerializer(mentor_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
