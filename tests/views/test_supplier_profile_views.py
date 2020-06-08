from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
from on_demand.models import SupplierProfile

class SupplierProfileTest(TestCase):
  # Creating one user with supplier profile
  @classmethod
  def setUpTestData(cls):
    user = get_user_model().objects.create_user(username='testuser@example.com', email='testuser@example.com', password='secret')
    supplier_profile, created = SupplierProfile.objects.get_or_create(user=user)

  def test_supplier_supplier_url_exists_at_desired_location(self):
    response = self.client.get('/users/1/supplier-profile/')
    self.assertEqual(response.status_code, 200)

  def test_supplier_profile_view_url_accesible_by_name(self):
    response = self.client.get(reverse('supplier-profile', args=[1]))
    self.assertEqual(response.status_code, 200)
