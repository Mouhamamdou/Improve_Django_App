from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Letting
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Renders the index page for lettings.

    Returns:
        HttpResponse: The response containing the rendered index page
    """
    lettings_list = get_list_or_404(Letting)
    context = {'lettings_list': lettings_list}
    try:
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error(f"An error occured: {e}")
        raise


def letting(request, letting_id):
    """
    Renders the letting detail page for a given letting ID.

    Returns:
        HttpResponse: The response containing the rendered letting detail page.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    try:
        return render(request, 'lettings/letting.html', context)
    except Exception as e:
        logger.error(f"An error occured: {e}")
        raise
