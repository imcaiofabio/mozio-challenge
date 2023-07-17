from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from app.models.provider import Provider
from app.models.service_area import ServiceArea


class EndpointTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.provider = Provider.objects.create(name='Provider1', email='provider1@example.com', phone_number='123456789', language='English', currency='USD')
        self.service_area = ServiceArea.objects.create(name='Service Area 1', price=10.99, provider=self.provider, area={
            "type": "Polygon",
            "coordinates": [[[0, 0], [0, 1], [1, 1], [1, 0], [0, 0]]]
        })

    def test_provider_list(self):
        url = reverse('provider-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_provider_detail(self):
        url = reverse('provider-detail', args=[self.provider.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_service_area_list(self):
        url = reverse('servicearea-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_service_area_detail(self):
        url = reverse('servicearea-detail', args=[self.service_area.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_polygon_lookup(self):
        lat, lng = 12.34, 56.78
        url = f'/polygons/?lat={lat}&lng={lng}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only one polygon matches the lat/lng pair

        polygon = response.data[0]
        self.assertEqual(polygon['name'], self.service_area.name)
        self.assertEqual(polygon['provider'], self.service_area.provider.id)
        self.assertEqual(polygon['price'], str(self.service_area.price))
