# Generated by Django 5.1 on 2024-08-28 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0002_auto_20240730_1027"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="letting",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
