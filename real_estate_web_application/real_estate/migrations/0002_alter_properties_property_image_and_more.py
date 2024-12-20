# Generated by Django 5.1.3 on 2024-11-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='property_image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='properties',
            name='type',
            field=models.CharField(choices=[('One Bedroom', 'One Bedroom'), ('Two Bedroom', 'Two Bedroom'), ('Three Bedroom', 'Three Bedroom'), ('Four Bedroom', 'Four Bedroom'), ('Maisonette', 'Maisonette'), ('Business Property', 'Business Property'), ('House', 'House'), ('Villa', 'Villa')], max_length=100),
        ),
    ]
