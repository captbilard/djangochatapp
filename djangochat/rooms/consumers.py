import json

from channels.generic.websocket import WebsocketConsumer

class RoomConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        text_data = json.dumps({
            'type':"connection_established",
            'message':'You are connected' 
        })
        self.send(text_data=text_data)
        

    # def receive(self, text_data=None, bytes_data=None):
    #     pass

    # def disconnect(self, code):
    #     pass