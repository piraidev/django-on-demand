from api.models import Mentorship, Message

def save_message(mentorship_id, from_id, to_id, message_text):
    mentorship = Mentorship.objects.get(id=mentorship_id)
    message = Message(mentorship=mentorship, sender_id=from_id, text=message_text)
    message.save()
    return message
