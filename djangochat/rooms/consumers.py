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
        # text_data = json.dumps({
        #     'type':"connection_established",
        #     'message':'You are connected' 
        # })
        # self.send(text_data=text_data)
        

    # def receive(self, text_data=None):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['content']

    #     self.send(text_data=json.dumps({
    #         'type': 'message',
    #         'message': message
    #     }))


    # def disconnect(self, code):
    #     pass