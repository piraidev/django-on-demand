from django.test import TestCase
from django.contrib.auth import get_user_model
from on_demand.models import SupplierProfile, UserDetails
from django.utils import timezone

class SupplierProfileTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    user = get_user_model().objects.create_user(username='testuser@example.com', email='testuser@example.com', password='secret')
    supplier_profile, created = SupplierProfile.objects.get_or_create(user=user)

  # Testing finished_connections_count default is 0
  def test_finished_connections_count_default(self):
    user_details = UserDetails.objects.get(id=1)
    supplier_profile = SupplierProfile.objects.get(user=user_details.user)
    finished_connections_count_default = supplier_profile._meta.get_field('finished_connections_count').default
    self.assertEquals(finished_connections_count_default, 0)

  # Testing connections_ranking_accumulator default is 0
  def test_connections_ranking_accumulator_default(self):
    user_details = UserDetails.objects.get(id=1)
    supplier_profile = SupplierProfile.objects.get(user=user_details.user)
    connections_ranking_accumulator = supplier_profile._meta.get_field('connections_ranking_accumulator').default
    self.assertEquals(connections_ranking_accumulator, 0)

  # Testing date_joined default is now (wihtin same minute)
  def test_date_joined_default(self):
    user_details = UserDetails.objects.get(id=1)
    supplier_profile = SupplierProfile.objects.get(user=user_details.user)
    date_joined = supplier_profile._meta.get_field('date_joined').default
    self.assertEqual(date_joined().year, timezone.now().year)
    self.assertEqual(date_joined().month, timezone.now().month)
    self.assertEqual(date_joined().day, timezone.now().day)
    self.assertEqual(date_joined().minute, timezone.now().minute)