# Generated by Django 3.0 on 2024-07-30 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name": "Address", "verbose_name_plural": "Addresses"},
        ),
    ]
