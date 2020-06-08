from django.test import TestCase
from django.contrib.auth import get_user_model
from on_demand.models import ConsumerProfile, UserDetails
from django.utils import timezone

class ConsumerProfileTest(TestCase):
  user_one_username = 'testuser@example.com'
  user_one_email = 'testuser@example.com'
  user_one_password = 'secret'
  user_one_first_name = 'FirstName'
  user_one_last_name = 'LastName'

  @classmethod
  def setUpTestData(cls):
    user = get_user_model().objects.create_user(username=ConsumerProfileTest.user_one_username, 
                                                email=ConsumerProfileTest.user_one_email,
                                                password=ConsumerProfileTest.user_one_password,
                                                first_name=ConsumerProfileTest.user_one_first_name,
                                                last_name=ConsumerProfileTest.user_one_last_name)
    consumer_profile, created = ConsumerProfile.objects.get_or_create(user=user)

  # Testing date_joined default is now (wihtin same minute)
  def test_date_joined_default(self):
    user_details = UserDetails.objects.get(id=1)
    consumer_profile = ConsumerProfile.objects.get(user=user_details.user)
    date_joined = consumer_profile._meta.get_field('date_joined').default
    self.assertEqual(date_joined().year, timezone.now().year)
    self.assertEqual(date_joined().month, timezone.now().month)
    self.assertEqual(date_joined().day, timezone.now().day)
    self.assertEqual(date_joined().minute, timezone.now().minute)
  
  def test_consumer_profile_object_name(self):
    user_details = UserDetails.objects.get(id=1)
    consumer_profile = ConsumerProfile.objects.get(user=user_details.user)
    expected_consumer_profile_name = f'Consumer: {consumer_profile.user.last_name}, {consumer_profile.user.first_name}'
    self.assertEquals(expected_consumer_profile_name, str(consumer_profile))