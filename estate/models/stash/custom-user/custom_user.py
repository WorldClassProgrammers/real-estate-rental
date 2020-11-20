from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from .owner import Owner


class CustomUser(AbstractUser):
    USER_TYPE = (
        (1, "visitor"),
        (2, "owner"),
    )

    role = models.PositiveSmallIntegerField(choices=USER_TYPE, default=2, null=True, blank=True)
    # owner = models.ForeignKey(Owner, default=None, null=True, blank=True, on_delete=models.CASCADE)
