from django.db import models


class TypeChoice(models.TextChoices):
    ONE_BEDROOM_APARTMENT = 'One-Bedroom Apartment', 'One-Bedroom Apartment'
    TWO_BEDROOM_APARTMENT = 'Two-Bedroom Apartment', 'Two-Bedroom Apartment'
    THREE_BEDROOM_APARTMENT = 'Three-Bedroom Apartment', 'Three-Bedroom Apartment'
    FOUR_BEDROOM_APARTMENT = 'Four-Bedroom Apartment', 'Four-Bedroom Apartment'
    MAISONETTE = 'Maisonette', 'Maisonette'
    BUSINESS_PROPERTY = 'Business Property', 'Business Property'
    HOUSE = 'House', 'House'
    VILLA = 'Villa', 'Villa'


