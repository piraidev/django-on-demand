from django.contrib.auth.models import User
from api.models import Notification
from api.signals import new_message
from django.conf import settings


class NotificationsHelper:

    @classmethod
    def create_notification(cls, user_id, from_id, role, notification_type, mentorship):
        Notification.objects.create(user_id=user_id, from_user_id=from_id, role=role, notification_type=notification_type, mentorship_id=mentorship.id)

    @classmethod
    def create_message_notification(cls, to_id, role, from_id, mentorship_id):
        new_messages_notifications = Notification.objects.filter(user_id=to_id, role=role, notification_type='new_message', viewed=False)
        if(new_messages_notifications.count() == 0):
            to_user = User.objects.get(id=to_id)
            from_user = User.objects.get(id=from_id)
            Notification.objects.create(user_id=to_id, from_user_id=from_id, role=role, notification_type='new_message', mentorship_id=mentorship_id)
            new_message.send(sender=cls, from_user=to_user.first_name, to_user=to_user.first_name)
    