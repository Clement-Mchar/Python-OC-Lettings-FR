from django.shortcuts import render
from .models import Profile
from sentry_sdk import capture_exception
import logging


def index(request):
    """
    View for the profile objects list :
    -Retrieves all of the objects in the profile table
    -Render them into the template
    args:
        request (HttpRequest) : the HTTP request object.

    returns:
        HttpResponse : the HTTP response object with the rendered template.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    View that displays a profile object :
    -Retrieves the object's infos by its id
    -Render it into the template
    args:
        request (HttpRequest) : the HTTP request object.
        profile_id : the requested object's id clicked on the previous page.
    returns:
        HttpResponse : the HTTP response object with the rendered template.
    """
    logger = logging.getLogger("django")
    try:
        profile = Profile.objects.get(user__username=username)
        context = {"profile": profile}
    except Exception as e:
        logger.warning(f"Error from the logger: {e}")
        capture_exception(e)
    return render(request, "profiles/profile.html", context)
