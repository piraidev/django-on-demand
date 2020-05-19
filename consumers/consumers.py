from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
import services.chat_service as chat_service
from serializers.serializers import MessageSerializer
from services import notifications_helper

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_text = text_data_json['message']
        mentorship_id = text_data_json['mentorship_id']
        from_id = text_data_json['from']
        to_id = text_data_json['to']
        to_role = text_data_json['to_role']

        message = chat_service.save_message(mentorship_id, from_id, to_id, message_text)
        notifications_helper.create_message_notification(to_id, to_role, from_id, mentorship_id)
        serialized_message = MessageSerializer(message)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': serialized_message.data
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))