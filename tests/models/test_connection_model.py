from django.test import TestCase
from django.contrib.auth import get_user_model
from on_demand.models import Connection, UserDetails
from django.utils import timezone

class ConnectionTest(TestCase):
  user_one_username = 'testuserone@example.com'
  user_one_email = 'testuserone@example.com'
  user_one_password = 'secret'
  user_one_first_name = 'OneFirstName'
  user_one_last_name = 'OneLastName'

  user_two_username = 'testusertwo@example.com'
  user_two_email = 'testusertwo@example.com'
  user_two_password = 'secret'
  user_two_first_name = 'TwoFirstName'
  user_two_last_name = 'TwoLastName'

  @classmethod
  def setUpTestData(cls):
    user_one = get_user_model().objects.create_user(username=ConnectionTest.user_one_username, 
                                                email=ConnectionTest.user_one_email,
                                                password=ConnectionTest.user_one_password,
                                                first_name=ConnectionTest.user_one_first_name,
                                                last_name=ConnectionTest.user_one_last_name)
    user_two = get_user_model().objects.create_user(username=ConnectionTest.user_two_username, 
                                                email=ConnectionTest.user_two_email,
                                                password=ConnectionTest.user_two_password,
                                                first_name=ConnectionTest.user_two_first_name,
                                                last_name=ConnectionTest.user_two_last_name)
    connection, created = Connection.objects.get_or_create(status='Some status', supplier=user_one, consumer=user_two)
  
  def test_consumer_profile_object_name(self):
    connection = Connection.objects.get(id=1)
    expected_connection_name = f'Connection {connection.id}. Supplier: {ConnectionTest.user_one_first_name}, {ConnectionTest.user_one_last_name}. Consumer: {ConnectionTest.user_two_first_name}, {ConnectionTest.user_two_last_name}'
    self.assertEquals(expected_connection_name, str(connection))