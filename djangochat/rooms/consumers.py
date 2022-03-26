import json

from channels.generic.websocket import WebsocketConsumer

class RoomConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            "type": "connection_established",
            "message": "We're connected"
        }))
        

    def receive(self, text_data=None, bytes_data=None):
        pass

    def disconnect(self, code):
        pass