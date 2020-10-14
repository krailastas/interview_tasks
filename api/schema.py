import graphene
from graphql import GraphQLError

from djangoTestAPI.redis_connect import redis_cache

from .graphql_types import PowerType
from .mutations import PowerMutation


class Query(graphene.ObjectType):
    get_active_power = graphene.Field(PowerType)
    get_reactive_power = graphene.Field(PowerType)

    def resolve_get_active_power(self, info):
        if redis_cache.exists('active'):
            return PowerType(value=redis_cache.get('active'))
        raise GraphQLError(
            'Active power does not exists. First you will need to run "createActiveReactivePower" mutation.'
        )

    def resolve_get_reactive_power(self, info):
        if redis_cache.exists('reactive'):
            return PowerType(value=redis_cache.get('reactive'))
        raise GraphQLError(
            'Reactive power does not exists. First you will need to run "createActiveReactivePower" mutation.'
        )


class Mutation(graphene.ObjectType):
    create_active_reactive_power = PowerMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
