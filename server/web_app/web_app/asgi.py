import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import main_app.urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_app.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            main_app.urls.websocket_urlpatterns
        )
    ),
})
