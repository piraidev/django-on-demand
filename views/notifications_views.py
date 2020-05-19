from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models.models import Notification
from serializers.serializers import NotificationSerializer
from rest_framework.permissions import AllowAny

@api_view(['GET'])
def get_notifications(request, user_id):
    try:
        role = request.GET.get('role')
        notifications = Notification.objects.filter(user_id=user_id, role=role).order_by('-date_created')[:7]
        if(not notifications):
            return Response([])
        notifications_serializer = NotificationSerializer(notifications, many=True)
        return Response(notifications_serializer.data)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def notifications_viewed(request, user_id):
    try:
        role = request.GET.get('role')
        notifications = Notification.objects.filter(user_id=user_id, role=role, viewed=False)
        if(not notifications):
            return Response([])
        for notification in notifications:
            notification.viewed = True
            notification.save()
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)

