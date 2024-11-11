from django.db import models


class TypeChoice(models.TextChoices):
    ONE_BEDROOM = 'One Bedroom', 'One Bedroom'
    TWO_BEDROOM = 'Two Bedroom', 'Two Bedroom'
    THREE_BEDROOM = 'Three Bedroom', 'Three Bedroom'
    FOUR_BEDROOM = 'Four Bedroom', 'Four Bedroom'
    MAISONETTE = 'Maisonette', 'Maisonette'
    BUSINESS_PROPERTY = 'Business Property', 'Business Property'
    HOUSE = 'House', 'House'
    VILLA = 'Villa', 'Villa'


