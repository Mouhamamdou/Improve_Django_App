from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def custom_error_500(request):
    """
    Custom view to handle server error (500).

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response containing the rendered 500 error page.
    """
    return render(request, '500.html', status=500)
