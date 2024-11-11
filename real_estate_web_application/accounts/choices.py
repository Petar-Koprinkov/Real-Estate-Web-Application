from django.db import models


class UserTypeChoice(models.TextChoices):
    BROKER = 'Broker', 'Broker',
    BUYER = 'Buyer', 'Buyer',
    INVESTOR = 'Investor', 'Investor',
    SELLER = 'Seller', 'Seller',
