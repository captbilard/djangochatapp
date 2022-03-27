import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class RoomConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f'chat_{self.room_name}'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None):
        data = json.loads(text_data)
        username = data['username']
        message = data['message']
        room = data['roomName']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': username,
                'message': message,
                'roomName': room,
            }
        )

    def chat_message(self, event):

        username = event['username']
        message = event['message']
        room = event['roomName']

        self.send(text_data=json.dumps({
            'username': username,
            'message': message,
            'room': room,
        }))
