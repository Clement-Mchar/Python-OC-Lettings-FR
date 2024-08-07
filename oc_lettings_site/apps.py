from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
    Configuration class for the oc_lettings_site app.

    This class is used to configure the Lettings application and set various
    options specific to this app. The `name` attribute defines the name of
    the application which is used by Django to reference it correctly.
    """
    name = "oc_lettings_site"
