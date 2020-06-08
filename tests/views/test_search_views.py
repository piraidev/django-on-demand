from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
from on_demand.models import SupplierProfile, UserDetails
from on_demand.serializers import SupplierProfileSerializer
import json

class NewestSuppliersTest(TestCase):
  def test_newest_suppliers_url_exists_at_desired_location(self):
    response = self.client.get('/api/newest-suppliers/')
    self.assertEqual(response.status_code, 200)

  def test_newest_suppliers_returns_empty_array_when_no_suppliers(self):
    response = self.client.get('/api/newest-suppliers/')
    self.assertEqual(response.status_code, 200)
    self.assertListEqual([], response.json())

  def test_newest_suppliers_view_url_accesible_by_name(self):
    response = self.client.get(reverse('newest-suppliers'))
    self.assertEqual(response.status_code, 200)

  def test_newest_suppliers_returns_single_result(self):
    # Creating one Supplier Profile from a user that has first_name, last_name and description
    user = get_user_model().objects.create_user(username='testuser@example.com', email='testuser@example.com', password='secret', first_name='hola', last_name='pianola')
    user_details = UserDetails.objects.get(id=1)
    user_details.description = 'Some test description'
    user_details.save(update_fields=['description'])
    supplier_profile, created = SupplierProfile.objects.get_or_create(user=user)
    
    # Calling view
    response = self.client.get(reverse('newest-suppliers'))

    # Calling  model (and serializer) to get all supplier profiles: one
    supplier_profiles_all = SupplierProfile.objects.all()
    supplier_profiles_all = SupplierProfileSerializer(supplier_profiles_all, many=True)
    
    self.assertEqual(response.status_code, 200)
    self.assertJSONEqual(response.content, supplier_profiles_all.data)

  def test_newest_suppliers_returns_max_30_results(self):
    # Creating 40 Supplier Profile from a user that has first_name, last_name and description
    for i in range(40):
      user = get_user_model().objects.create_user(username=f'testuser.{i}@example.com', email=f'testuser.{i}@example.com', password='secret', first_name=f'hola-{i}', last_name=f'pianola{i}')
      user_details = UserDetails.objects.get(id=i + 1)
      user_details.description = f'Some test description for user {i}'
      user_details.save(update_fields=['description'])
      supplier_profile, created = SupplierProfile.objects.get_or_create(user=user)
    
    # Calling view
    response = self.client.get(reverse('newest-suppliers'))

    # Calling  model (and serializer) to get all supplier profiles: one
    supplier_profiles_all = SupplierProfile.objects.all()
    supplier_profiles_all = SupplierProfileSerializer(supplier_profiles_all, many=True)

    # Asserting that despite having 40 Supplier Profiles only first 30 are returnes
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(json.loads(response.content.decode('utf-8'))), 30)