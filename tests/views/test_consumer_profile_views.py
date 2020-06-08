from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
from on_demand.models import ConsumerProfile

class ConsumerProfileTest(TestCase):
  # Creating one user with consumer profile
  @classmethod
  def setUpTestData(cls):
    user = get_user_model().objects.create_user(username='testuser@example.com', email='testuser@example.com', password='secret')
    consumer_profile, created = ConsumerProfile.objects.get_or_create(user=user)

  def test_consumer_supplier_url_exists_at_desired_location(self):
    response = self.client.get('/users/1/consumer-profile/')
    self.assertEqual(response.status_code, 200)

  def test_consumer_profile_view_url_accesible_by_name(self):
    response = self.client.get(reverse('consumer-profile', args=[1]))
    self.assertEqual(response.status_code, 200)
