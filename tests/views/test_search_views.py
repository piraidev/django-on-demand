from django.test import TestCase
from django.urls import reverse


class NewestSuppliersTest(TestCase):
    def test_newest_suppliers_url_exists_at_desired_location(self):
        response = self.client.get('/api/newest-suppliers/')
        self.assertEqual(response.status_code, 200)

    def test_newest_suppliers_returns_empty_array_when_no_suppliers(self):
        response = self.client.get('/api/newest-suppliers/')
        self.assertEqual(response.status_code, 200)
        self.assertListEqual([], response.json())
