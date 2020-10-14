import pytest

from channels.testing import WebsocketCommunicator
from channels.layers import get_channel_layer
from django.conf import settings

from .notifications import Notifications


@pytest.mark.asyncio
async def test_notification():
    communicator = WebsocketCommunicator(application=Notifications, path='/ws/notification/')
    connected, test = await communicator.connect()
    assert connected
    channel_layer = get_channel_layer()
    message = {'active_power': 0.2, 'reactive_power': 0.01}
    await channel_layer.group_send(settings.NOTIFICATION_GROUP,
                                   {'type': 'send_notifications',
                                    'message': message})
    assert {'message': message} == await communicator.receive_json_from(timeout=10)
    await communicator.disconnect()
