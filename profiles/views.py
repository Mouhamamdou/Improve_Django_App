from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Profile


def index(request):
    """
    Renders the index page for profiles.

    Returns:
        HttpResponse: The response containing the rendered index page
    """
    profiles_list = get_list_or_404(Profile)
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Renders the profile page for a given user.

    Returns:
        HttpResponse: The response containing the rendered profile page.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)