from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models.models import ContactMessage, User

@api_view(['POST'])
def register_contact_message(request):
    try:
        message = request.data['message']
        user = request.auth.user
        contact_message = ContactMessage(user=user, message=message)
        contact_message.save()
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)

