from django.db import models
from multiselectfield import MultiSelectField

class Condo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500)
    # condo_image = models.ImageField()
    number_of_floors = models.IntegerField(default=1)

    # admin only
    juristic_persons_number = models.TextField(max_length=25)
    common_fee_account = models.TextField(max_length=25)

    # # amenities
    # elevator = models.BooleanField(default=False)
    # parking_lot = models.BooleanField(default=False)
    # cctv = models.BooleanField(default=False)
    # security = models.BooleanField(default=False)
    # wifi = models.BooleanField(default=False)
    # swimming_pool = models.BooleanField(default=False)
    # sauna = models.BooleanField(default=False)
    # garden = models.BooleanField(default=False)
    # playground = models.BooleanField(default=False)
    # gym = models.BooleanField(default=False)
    # shop_on_premise = models.BooleanField(default=False)
    # restaurant_on_premise = models.BooleanField(default=False)

    # location = models.CharField(
    #     max_length=200,
    #     validators=[
    #         RegexValidator(regex='^(-?\d+(\.\d+)?),\s*(-?\d+(\.\d+)?)$',
    #         message='Must be a valid GPS coordination.'),
    #     ])

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

    amenities = MultiSelectField(
        choices=AMENITY_TYPES, default=None,
        )

    def __str__(self):
        """Return the name of the condo."""
        return self.name

    def get_rooms(self):
        rooms = self.room_set.all()
        return rooms