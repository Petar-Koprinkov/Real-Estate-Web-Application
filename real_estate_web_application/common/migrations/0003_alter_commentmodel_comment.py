# Generated by Django 5.1.3 on 2024-12-03 08:09

import real_estate_web_application.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_rename_content_commentmodel_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='comment',
            field=models.TextField(validators=[real_estate_web_application.common.validators.BadLanguageValidator]),
        ),
    ]
