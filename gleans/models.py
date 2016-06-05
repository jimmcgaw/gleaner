from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

CROP_CHOICES = (
    ('b', 'Backyard Grower'),
    ('f', 'Commercial Farmer'),
)

RECEIPT_PREFERENCES = (
    ('e', 'Email'),
    ('m', 'Mail'),
)

class Crop(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=20) # validators should be a list
    user = models.ForeignKey('auth.User')

    contact_address1 = models.CharField(max_length=50)
    contact_address2 = models.CharField(max_length=50, blank=True)
    contact_city = models.CharField(max_length=50)
    contact_state = models.CharField(max_length=20)
    contact_zip = models.CharField(max_length=10)

    crop_address1 = models.CharField(max_length=50, blank=True)
    crop_address2 = models.CharField(max_length=50, blank=True)
    crop_city = models.CharField(max_length=50, blank=True)
    crop_state = models.CharField(max_length=20, blank=True)
    crop_zip = models.CharField(max_length=10, blank=True)

    crop_type = models.CharField(max_length=1, choices=CROP_CHOICES)
    receipt_preference = models.CharField(max_length=1, choices=RECEIPT_PREFERENCES)

    crop_description = models.TextField()

    # internal use by the food bank only
    equipment_needed = models.TextField()
    load_in = models.TextField()
    bathroom_available = models.BooleanField(default=False)
    power_lines = models.TextField()
    pets = models.TextField()
