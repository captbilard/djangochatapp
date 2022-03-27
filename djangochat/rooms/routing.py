from django.urls import URLPattern, path
from .consumers import RoomConsumer

websocket_urlpatterns = [
    path('ws/<str:room_name>/', RoomConsumer.as_asgi()),
]