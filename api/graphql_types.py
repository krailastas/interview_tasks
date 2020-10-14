import graphene


class PowerType(graphene.ObjectType):
    value = graphene.Float()
