from django.test import TestCase
from graphene.test import Client

from api.schema import schema


class TestBlogSchema(TestCase):
    def setUp(self):
        self.client = Client(schema)

    def test_create_power_query(self):
        mutations_create_power = """
            mutation {
              createActiveReactivePower {
                activeValue
                reactiveValue
              }
            }
        """
        response = self.client.execute(mutations_create_power)
        response_data = response.get('data').get('createActiveReactivePower')
        assert response_data['activeValue']
        assert response_data['reactiveValue']

    def test_get_active_power(self):
        query_get_active_power = """
            query {
              getActivePower{
                value
              }
            }
        """
        response = self.client.execute(query_get_active_power)
        response_data = response.get('data').get('getActivePower')
        assert response_data['value']

    def test_get_reactive_power(self):
        query_get_reactive_power = """
            query {
              getReactivePower{
                value
              }
            }
        """
        response = self.client.execute(query_get_reactive_power)
        response_data = response.get('data').get('getReactivePower')
        assert response_data['value']
