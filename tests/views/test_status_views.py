from django.test import TestCase

class StatusViewTest(TestCase):
  def test_status_url_exists_at_desired_location(self):
    response = self.client.get('/api/status/')
    self.assertEqual(response.status_code, 200)