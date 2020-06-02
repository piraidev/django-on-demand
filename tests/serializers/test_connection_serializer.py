import json
from django.test import TestCase
from django.contrib.auth import get_user_model
from on_demand.models import UserDetails, Connection
from on_demand.serializers import ConnectionSerializer


class ConnectionSerializerTest(TestCase):

  def test_connection_deserialization(self):
    supplier = get_user_model().objects.create_user(username='supplier@domain.com', email='supplier@domain.com', password='Supplier123')
    consumer = get_user_model().objects.create_user(username='consumer@domain.com', email='consumer@domain.com', password='Consumer123')
    connection = Connection.objects.create(supplier=supplier,consumer=consumer,status='requested')
    connection = Connection.objects.get(id=1)
    deserialized_connection = ConnectionSerializer(connection)
    expected_deserialized = "{'id': 1, 'supplier': 1, 'consumer': 2, 'status': 'requested', 'date_created': '" + connection.date_created.isoformat() +"', 'date_finished': None, 'objective': '', 'rejection_reason': None, 'consumer_request_comments': None, 'finish_reason': None, 'ranking': None}"
    self.assertEquals(expected_deserialized, str(deserialized_connection.data))
    