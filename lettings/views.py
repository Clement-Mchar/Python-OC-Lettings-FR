from django.shortcuts import render
from .models import Letting
from sentry_sdk import capture_exception
import logging

# Create your views here.


def index(request):
    """
    View for the letting objects list :
    -Retrieves all of the objects in the letting table
    -Render them into the template
    args:
        request (HttpRequest) : the HTTP request object.

    returns:
        HttpResponse : the HTTP response object with the rendered template.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    View that displays a letting object :
    -Retrieves the object's infos by its id
    -Render it into the template
    args:
        request (HttpRequest) : the HTTP request object.
        letting_id : the requested object's id.
    returns:
        HttpResponse : the HTTP response object with the rendered template.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    Exceptions are caught by sentry and logged
    """
    logger = logging.getLogger("django")
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
    except Exception as e:
        logger.warning(f"Error from the logger: {e}")
        capture_exception(e)
    return render(request, "lettings/letting.html", context)
