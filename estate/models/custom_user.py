from django.contrib.auth.models import AbstractUser
from django.db import models
from .owner import Owner


class CustomUser(AbstractUser):
    USER_TYPE = (
        (1, "visitor"),
        (2, "owner"),
    )

    role = models.PositiveSmallIntegerField(choices=USER_TYPE)
    owner = models.ForeignKey(Owner, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_user'
