import json

from django.conf import settings

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class Notifications(AsyncJsonWebsocketConsumer):
    async def send_notifications(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def connect(self):
        await self.channel_layer.group_add(settings.NOTIFICATION_GROUP, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            settings.NOTIFICATION_GROUP,
            self.channel_name
        )
