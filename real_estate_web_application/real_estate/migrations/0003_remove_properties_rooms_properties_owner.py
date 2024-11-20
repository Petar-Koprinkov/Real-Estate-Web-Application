# Generated by Django 5.1.3 on 2024-11-20 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_email'),
        ('real_estate', '0002_alter_properties_property_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='rooms',
        ),
        migrations.AddField(
            model_name='properties',
            name='owner',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, related_name='property', to='accounts.profile'),
            preserve_default=False,
        ),
    ]
