# Generated by Django 5.1.3 on 2024-11-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0006_location_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='type',
            field=models.CharField(choices=[('One-Bedroom', 'One-Bedroom'), ('Two Bedroom', 'Two Bedroom'), ('Three Bedroom', 'Three Bedroom'), ('Four Bedroom', 'Four Bedroom'), ('Maisonette', 'Maisonette'), ('Business Property', 'Business Property'), ('House', 'House'), ('Villa', 'Villa')], max_length=100),
        ),
    ]
