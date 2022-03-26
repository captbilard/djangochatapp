from django.urls import URLPattern, re_path
from .consumers import RoomConsumer

websocket_urlpatterns = [
    re_path('ws/socket-server', RoomConsumer.as_asgi())
]