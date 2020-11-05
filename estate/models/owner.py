from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100)
    # email = models.EmailField(max_length=100)
    # line_id = models.CharField(max_length=100)
    # phone_number = models.CharField(max_length=100)

    def __str__(self):
        """Return the name of the owner."""
        return self.name


class ContactInfo(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    CONTACT_TYPES = (
        ('phone', 'Phone Number'),
        ('email', 'Email Address'),
        ('line', 'Line Id'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
    )
    contact_type = models.CharField(
        choices=CONTACT_TYPES,
        default='phone',
        max_length=10,
    )
    information = models.CharField(max_length=100)
