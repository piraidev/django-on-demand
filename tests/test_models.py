from django.test import TestCase

from on_demand.models import UserDetails

class UserDetailsTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    UserDetails.objects.create(email='somemail@domain.com')

  # Testin label for field defined
  def test_email_label(self):
    user = UserDetails.objects.get(id=1)
    email_label = user._meta.get_field('email').verbose_name
    self.assertEquals(email_label, 'email')