from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from real_estate_web_application.accounts.models import Profile
from django.contrib.auth.models import Group

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=UserModel)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "Buyer":
            group = Group.objects.get(name="Buyer")
        elif instance.user_type == "Seller":
            group = Group.objects.get(name="Seller")
        elif instance.user_type == "Broker":
            group = Group.objects.get(name="Broker")
        else:
            group = Group.objects.get(name="Investor")

        instance.groups.add(group)
