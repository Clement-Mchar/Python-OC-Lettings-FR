"""
Configuration class for the profiles app.
This class is used to configure the Profiles application and set various
options specific to this app. The `name` attribute defines the name of
the application which is used by Django to reference it correctly.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):

    name = "profiles"
