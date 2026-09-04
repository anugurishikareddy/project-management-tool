import json

from channels.generic.websocket import AsyncWebsocketConsumer


class TaskConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

        await self.send(text_data=json.dumps({
            "type": "connection",
            "message": "WebSocket Connected Successfully"
        }))

    async def disconnect(self, close_code):
        print("WebSocket disconnected:", close_code)

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message = data.get("message", "")
        except json.JSONDecodeError:
            message = text_data

        await self.send(text_data=json.dumps({
            "type": "message",
            "message": message
        }))