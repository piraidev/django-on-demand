from django.test import TestCase
from django.contrib.auth import get_user_model
from on_demand.models import UserDetails

class UserDetailsTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    user = get_user_model().objects.create_user(username='testuser@example.com', email='testuser@example.com', password='secret')
    user = UserDetails.objects.get(id=1)
    user.picture = 'SomePictureURL'
    user.save(update_fields=['picture'])
    

  # Testing label for field defined
  def test_email_label(self):
    user = UserDetails.objects.get(id=1)
    email_label = user._meta.get_field('email').verbose_name
    self.assertEquals(email_label, 'email')
  
  # Testing email field is unique
  def test_email_is_unique(self):
    user = UserDetails.objects.get(id=1)
    email_uniqueness = user._meta.get_field('email').unique
    self.assertEquals(email_uniqueness, True)

  # Testing label for field defined
  def test_picture_label(self):
    user = UserDetails.objects.get(id=1)
    picture_label = user._meta.get_field('picture').blank
    self.assertEquals(picture_label, True)