import graphene

from django.conf import settings
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from djangoTestAPI.redis_connect import redis_cache
from djangoTestAPI.test_sim import run_simulation


class PowerMutation(graphene.Mutation):
    active_value = graphene.Float()
    reactive_value = graphene.Float()

    def mutate(self, info):
        active_power, reactive_power = run_simulation()
        redis_cache.set('active', active_power)
        redis_cache.set('reactive', reactive_power)
        # Send new data to ws channel
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            settings.NOTIFICATION_GROUP, {'type': 'send_notifications',
                                          'message': {'active_power': active_power, 'reactive_power': reactive_power}})
        return PowerMutation(active_value=active_power, reactive_value=reactive_power)
