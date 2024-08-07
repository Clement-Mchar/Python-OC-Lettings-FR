from django.contrib import admin

from .models import Profile

"""
Adds models and their associated tables and data to the admin page
"""

admin.site.register(Profile)
