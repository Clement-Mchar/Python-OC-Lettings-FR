from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model that extends the default Django User model to include
    additional information about the user.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the Django User model.
        favorite_city (CharField): An optional field to store the user's favorite city.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
