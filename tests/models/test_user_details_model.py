from django.test import TestCase
from django.contrib.auth import get_user_model
from on_demand.models import UserDetails

class UserDetailsTest(TestCase):
  user_one_username = 'testuser@example.com'
  user_one_email = 'testuser@example.com'
  user_one_password = 'secret'
  user_one_first_name = 'FirstName'
  user_one_last_name = 'LastName'

  @classmethod
  def setUpTestData(cls):
    user = get_user_model().objects.create_user(username=UserDetailsTest.user_one_username, 
                                                email=UserDetailsTest.user_one_email,
                                                password=UserDetailsTest.user_one_password,
                                                first_name=UserDetailsTest.user_one_first_name,
                                                last_name=UserDetailsTest.user_one_last_name)
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
  
  def test_user_details_object_name(self):
    user = UserDetails.objects.get(id=1)
    expected_user_details_name = f'User details: {UserDetailsTest.user_one_last_name}, {UserDetailsTest.user_one_first_name}'
    self.assertEquals(expected_user_details_name, str(user))