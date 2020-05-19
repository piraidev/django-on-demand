from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url

from consumers import consumers

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer)
        )
    ),
})