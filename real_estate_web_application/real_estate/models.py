from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from real_estate_web_application.accounts.models import Profile
from real_estate_web_application.real_estate.choices import TypeChoice


UserModel = get_user_model()


class Properties(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    type = models.CharField(
        max_length=100,
        choices=TypeChoice.choices,

    )

    property_image = models.URLField()

    floors = models.IntegerField()

    exposure = models.CharField(
        max_length=100,
    )

    value = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(0.0, message='Value must be greater than zero')],
    )

    location = models.ForeignKey(
        to='Location',
        on_delete=models.CASCADE,
        related_name='properties',
    )

    parking = models.ForeignKey(
        to='Parking',
        related_name='properties',
        on_delete=models.CASCADE,
    )

    content = models.TextField()

    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='property',
    )

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.CharField(
        max_length=100,
    )

    state = models.CharField(
        max_length=100,
    )

    postcode = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return f'{self.city}, {self.state}'


class Parking(models.Model):

    parking_name = models.CharField(
        max_length=100,
    )

    parking_slots = models.PositiveIntegerField()

    location = models.ForeignKey(
        to='Location',
        on_delete=models.CASCADE,
        related_name='parking',
    )

    def __str__(self):
        return self.parking_name















