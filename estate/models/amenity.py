from django.db import models
from .condo import Condo

class Amenity(models.Model):
    # amenities
    condo = models.ForeignKey(Condo, on_delete=models.RESTRICT)

    AMENITY_TYPES = (
        ('elevator', 'Elevator'),
        ('parking_lot', 'Parking Lot'),
        ('cctv', 'CCTV'),
        ('security', 'Security'),
        ('wifi', 'WiFi'),
        ('swimming_pool', 'Swimming Pool'),
        ('sauna', 'Sauna'),
        ('garden', 'Garden'),
        ('playground', 'Playground'),
        ('gym', 'Gym'),
        ('shop', 'Shop'),
        ('restaurant', 'Restaurant'),
    )

    kind = models.CharField(
        max_length=20,
        choices=AMENITY_TYPES,
        blank=True,
        default=None,
        help_text='Amenity type',
    )

    status = models.BooleanField(
        default=False
    )
