from django.db import models


class Condo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500)
    number_of_floors = models.IntegerField(default=1)
    # amenities = ...
    elevator = models.BooleanField(default=False)
    parking_lot = models.BooleanField(default=False)  # should change to integer?
    # ...
    # location = models.CharField(
    #     max_length=200,
    #     validators=[
    #         RegexValidator(regex='^(-?\d+(\.\d+)?),\s*(-?\d+(\.\d+)?)$',
    #         message='Must be a valid GPS coordination.'),
    #     ])


class Room(models.Model): # Unit
    condo = models.ForeignKey(Condo, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.RESTRICT)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.FloatField(default=0)
    floor_number = models.CharField(max_length=10, default="1")  # in case of "12A"
    room_number = models.CharField(max_length=10, default="1")
    number_of_bedroom = models.IntegerField(default=1)
    number_of_bathroom = models.IntegerField(default=1)
    area = models.FloatField(default=0)  # in square meters?


class RoomImages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField()  # needs to limit image size?


class Owner(models.Model):
    name = models.CharField(max_length=100)
    # ...
