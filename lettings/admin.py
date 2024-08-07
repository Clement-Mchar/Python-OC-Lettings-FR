from django.contrib import admin

from .models import Letting
from .models import Address

"""
Adds models and their associated tables and data to the admin page
"""

admin.site.register(Letting)
admin.site.register(Address)
