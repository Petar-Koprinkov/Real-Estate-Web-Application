from django.core.validators import MinValueValidator
from django.db import models
from real_estate_web_application.accounts.models import Profile
from real_estate_web_application.real_estate.choices import TypeChoice


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

    content = models.TextField()

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='property',
    )


class Location(models.Model):
    city = models.CharField(
        max_length=100,
    )

    state = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return f'{self.city}, {self.state}'













