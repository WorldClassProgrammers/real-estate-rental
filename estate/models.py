from django.db import models


class Condo(models.Model):
    condo_name = models.CharField(max_length=200)
    # ...


class Room(models.Model):
    condo = models.ForeignKey(Condo, on_delete=models.CASCADE)
    # ...
