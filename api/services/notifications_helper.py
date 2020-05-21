from django.contrib.auth.models import User
from api.models import Notification
import api.services.email_service as email_service
from django.conf import settings

def create_notification(user_id, from_id, role, notification_type, mentorship):
    Notification.objects.create(user_id=user_id, from_user_id=from_id, role=role, notification_type=notification_type, mentorship_id=mentorship.id)

def create_message_notification(to_id, role, from_id, mentorship_id):
    new_messages_notifications = Notification.objects.filter(user_id=to_id, role=role, notification_type='new_message', viewed=False)
    if(new_messages_notifications.count() == 0):
        to_user = User.objects.get(id=to_id)
        from_user = User.objects.get(id=from_id)
        Notification.objects.create(user_id=to_id, from_user_id=from_id, role=role, notification_type='new_message', mentorship_id=mentorship_id)
        email_service.send_email(to_user.profile.email, settings.SENGRID_NEW_MESSAGE_TEMPLATE_ID, {'to_name': to_user.first_name, 'from_name': from_user.first_name})