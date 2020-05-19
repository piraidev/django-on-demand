from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models.models import Mentorship, Message
from serializers.serializers import MessageSerializer
from rest_framework.permissions import AllowAny

@api_view(['GET'])
def get_messages(request, mentorship_id):
    try:
        mentorship = Mentorship.objects.get(id=mentorship_id)
        if(not mentorship):
            return Response([])
        messages = Message.objects.filter(mentorship=mentorship)
        messages_serialized = MessageSerializer(messages, many=True)
        return Response(messages_serialized.data)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
