from django.urls import path

from . import views

app_name = "lettings"

"""
URL configuration for the Lettings app.

This module defines the URL patterns for the Lettings application.
It maps URLs to views, allowing the app to respond to different HTTP
requests at specific endpoints.
The 'app_name' attribute is used to identify the app in other urls.py files

Routes:
- '' : maps to the index view, which displays a list of lettings.
- '<int:letting_id>/': maps to the letting view, which displays
  details of a specific letting identified by its ID.
"""

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
