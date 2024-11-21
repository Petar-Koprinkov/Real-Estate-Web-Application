# Generated by Django 5.1.3 on 2024-11-21 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0004_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='address',
        ),
        migrations.RemoveField(
            model_name='properties',
            name='city',
        ),
        migrations.AddField(
            model_name='properties',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='real_estate.location'),
            preserve_default=False,
        ),
    ]
