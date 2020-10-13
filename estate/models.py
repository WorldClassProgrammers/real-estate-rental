from django.db import models


class Condo(models.Model):
    condo_name = models.CharField(max_length=100, unique=True)
    condo_description = models.TextField(max_length=500)
    # condo_image = models.ImageField()
    number_of_floors = models.IntegerField(default=1)

    # amenities
    elevator = models.BooleanField(default=False)
    parking_lot = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    sauna = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    playground = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    shop_on_premise = models.BooleanField(default=False)
    restaurant_on_premise = models.BooleanField(default=False)

    # location = models.CharField(
    #     max_length=200,
    #     validators=[
    #         RegexValidator(regex='^(-?\d+(\.\d+)?),\s*(-?\d+(\.\d+)?)$',
    #         message='Must be a valid GPS coordination.'),
    #     ])

    def __str__(self):
        """Return the name of the condo."""
        return self.condo_name

    def get_rooms(self):
        rooms = self.room_set.all() # still not work

        # rooms = Room.objects.filter(
        #     condo_name=self.condo_name
        # )

        return rooms


class Owner(models.Model):
    owner_name = models.CharField(max_length=100)
    owner_email = models.EmailField(max_length=100)
    owner_line_id = models.CharField(max_length=100)
    owner_phone_number = models.IntegerField(default=0)

    def __str__(self):
        """Return the name of the owner."""
        return self.owner_name


class Room(models.Model):
    condo_name = models.ForeignKey(Condo, on_delete=models.CASCADE)
    owner_name = models.ForeignKey(Owner, on_delete=models.RESTRICT)
    room_number = models.CharField(max_length=10, default="1")
    room_title = models.CharField(max_length=100)
    room_description = models.TextField(max_length=500)
    # room_image = models.ImageField()
    still_on_contract = models.BooleanField(default=False)
    price_for_rent = models.FloatField(default=0)
    price_for_sell = models.FloatField(default=0)
    number_of_floor = models.CharField(max_length=10, default="1")
    number_of_bedroom = models.IntegerField(default=1)
    number_of_bathroom = models.IntegerField(default=1)
    area = models.FloatField(default=0)  # in square meters? -> sure

    def __str__(self):
        """Return the title of the room."""
        return self.room_title


# class RoomImages(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     image = models.ImageField()  # needs to limit image size? -> no
