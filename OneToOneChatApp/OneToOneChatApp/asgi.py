import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import ChatRoom.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OneToOneChatApp.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(), 
    "websocket": AuthMiddlewareStack(
        URLRouter(
            ChatRoom.routing.websucket_urlpatterns
        )
    )
    }
)