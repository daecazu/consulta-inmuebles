from django.test import TestCase
# models imports
from inmuebles.models import Property
from inmuebles.models import Status
from inmuebles.models import StatusHistory

def sample_property(
    address = 'calle 23 #45-67',
    city = 'Bogota',
    price = 120000000,
    description = 'Hermoso apartamento'/
        'en el centro de la ciudad',
    year = 2000
):
    """ Create a sample property"""
    return Property.objects.create(
        address=address,
        city=city,
        price=price,
        description=description,
        year=year
    )

def sample_status(
    name='pre_venta',
    label='Inmueble publicado en preventa'
):
    """ Create a sample status"""
    return Status.objects.create(
        name=name,
        label=label
    )


class ModelTests(TestCase):
    """
    model testing
    """
    def setUp(self):
        self.bogota_property = sample_property()
        self.status = sample_status()
        self.status_history = StatusHistory.objects.create(
            property = self.bogota_property,
            status = self.status,
            update_date = '2021-04-10 22:23:56'
        )

    def test_property_str(self):
        """
        test property table has a string representation
        """
        self.assertEqual(
            str(self.bogota_property),
            f'address:{self.bogota_property.adress}'
        )

    def test_status_str(self):
        """
        test status table has a string representation
        """
        self.assertEqual(
            str(self.status),
            f'status:{self.status.name}'   
        )
    def test_status_history_str(self):
        """
        test status table has a string representation
        """
        self.assertEqual(
            str(self.status_history),
            f'date:{self.status_history.update_date}'   
        )