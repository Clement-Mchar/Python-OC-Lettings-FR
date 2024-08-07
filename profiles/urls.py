from django.urls import path

from . import views

app_name = "profiles"
"""
URL configuration for the Profiles app.

This module defines the URL patterns for the profiles application.
It maps URLs to views, allowing the app to respond to different HTTP
requests at specific endpoints.
The 'app_name' attribute is used to identify the app in other urls.py files

Routes:
- '' : maps to the index view, which displays a list of profiles.
- '<str:username>/': maps to the profile view, which displays
  details of a specific profile identified by its ID.
"""
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:username>/", views.profile, name="profile"),
]
