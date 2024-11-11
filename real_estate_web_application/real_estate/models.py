from django.core.validators import MinValueValidator
from django.db import models


class Properties(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    type = models.CharField(
        max_length=100,
        choices=[]
    )

    property_image = models.ImageField(
        upload_to='property_image/',
    )

    rooms = models.IntegerField()

    floors = models.IntegerField()

    exposure = models.CharField(
        max_length=100,
    )

    value = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(0.0, message='Value must be greater than zero')],
    )

    address = models.CharField(
        max_length=100,
        unique=True,
    )

    city = models.CharField(
        max_length=100,
    )

    content = models.TextField()