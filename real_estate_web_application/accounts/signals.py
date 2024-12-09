from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from real_estate_web_application.accounts.models import Profile
from django.contrib.auth.models import Group, Permission

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def assign_permissions(group_name, perm_list):
    group, created = Group.objects.get_or_create(name=group_name)
    permissions = Permission.objects.filter(codename__in=perm_list)
    group.permissions.set(permissions)
    return group


@receiver(post_save, sender=UserModel)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.is_staff = True

        if instance.user_type == "Buyer":
            perm_list = ['view_customuser', 'view_profile', 'add_commentmodel', 'view_commentmodel', 'view_contenttype',
                         'view_location', 'view_parking', 'view_property']
            group = assign_permissions("Buyer", perm_list)
        elif instance.user_type == "Seller":
            perm_list = ['view_customuser', 'view_profile', 'view_commentmodel', 'view_contenttype', 'view_location',
                         'add_location', 'change_location', 'delete_location', 'view_parking', 'add_parking',
                         'delete_parking', 'view_property', 'change_parking', 'change_property', 'delete_property',
                         'add_property']
            group = assign_permissions("Seller", perm_list)
        elif instance.user_type == "Broker":
            perm_list = ['view_customuser', 'view_profile', 'view_commentmodel', 'add_commentmodel', 'view_contenttype',
                         'view_location', 'add_location', 'change_location', 'delete_location', 'view_parking',
                         'add_parking', 'delete_parking', 'change_parking', 'view_property', 'change_property',
                         'delete_property', 'add_property']
            group = assign_permissions("Broker", perm_list)
        elif instance.user_type == "Investor":
            perm_list = ['view_customuser', 'view_profile', 'view_commentmodel', 'view_contenttype',
                         'view_location', 'add_location', 'change_location', 'delete_location', 'view_parking',
                         'add_parking', 'delete_parking', 'change_parking', 'view_properties', 'add_properties',
                         'change_properties', 'delete_properties']
            group = assign_permissions("Investor", perm_list)

        instance.groups.add(group)
        instance.save()
