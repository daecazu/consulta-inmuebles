# Django Test imports
from django.urls import reverse
from django.test import TestCase

# Django Rest Framework imports
from rest_framework import status
from rest_framework.test import APIClient

# models imports
from inmuebles.models import StatusHistory

# test samples
from .test_models import sample_property
from .test_models import sample_status


INMUEBLES_URL = reverse('inmuebles:inmuebles-list')


class InmueblesApiTest(TestCase):

    def setUp(self):
        """
        creating base data to test
        property 1 status comprando
        property 2 status pre_venta
        property 3 status en_venta

        """
        self.client = APIClient()
        # creating properties
        self.property_1 = sample_property()
        self.property_2 = sample_property(
            address='carrera 100 #15-90',
            city='medellin',
            price=325000000,
            description=(
                'Amplio apartamento en conjunto cerrado'
            ),
            year=2011
        )
        self.property_3 = sample_property(
            address='calle 23 #45-67',
            city='medellin',
            price=210000000,
            description='',
            year=2002
        )
        # creating 3 property status
        self.status_1 = sample_status()
        self.status_2 = sample_status(
            name='comprando',
            label='Imueble en proceso de compra'
        )
        self.status_3 = sample_status(
            name='en_venta',
            label='Inmueble publicado en venta'
        )
        # creating a status history for property 1
        self.status_history_old = StatusHistory.objects.create(
            property=self.property_1,
            status=self.status_1,
            update_date='2021-03-10 22:23:56'
        )
        self.status_history_latest = StatusHistory.objects.create(
            property=self.property_1,
            status=self.status_2,
            update_date='2021-04-10 22:23:56'
        )
        # creating a status_history for property 2 and 3
        self.status_history_property_2 = StatusHistory.objects.create(
            property=self.property_2,
            status=self.status_1,
            update_date='2021-03-11 22:23:56'
        )
        self.status_history_property_2 = StatusHistory.objects.create(
            property=self.property_3,
            status=self.status_3,
            update_date='2021-05-09 22:23:56'
        )

    def test_get_inmuebles(self):
        """
        test (get) endpoint results
        """
        expected_json = [
            {
                "property": {
                    'address': 'carrera 100 #15-90',
                    'city': 'medellin',
                    'price': 325000000,
                    'description':
                    'Amplio apartamento en conjunto cerrado',
                    'year': 2011
                },

                'status': {
                    'name': 'pre_venta'
                }
            },
            {
                "property": {
                    'address': 'calle 23 #45-67',
                    'city': 'medellin',
                    'price': 210000000,
                    'description': '',
                    'year': 2002
                },
                'status':  {
                    'name':  'en_venta'
                }
            }
        ]

        response = self.client.get(INMUEBLES_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_json)

    def test_get_search_inmuebles(self):
        payload = {
            'city': 'medellin',
            'status': 'en_venta',
            'year': '2002'
        }
        response = self.client.get(
            INMUEBLES_URL,
            payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
