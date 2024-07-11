from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Letting


def index(request):
    """
    Renders the index page for lettings.

    Returns:
        HttpResponse: The response containing the rendered index page
    """
    lettings_list = get_list_or_404(Letting)
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


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
    return render(request, 'lettings/letting.html', context)