import pytest
from django.contrib.auth.models import User
from .models import Profile
from django.test import Client
from django.urls import reverse, resolve
from .views import index, profile


@pytest.mark.django_db
def test_profile_mdoel():
    user = User.objects.create(
        username="Moussa"
        )
    profile = Profile.objects.create(
        user=user,
        favorite_city="Paris"
        )
    assert profile.user == user
    assert profile.favorite_city == "Paris"


@pytest.mark.django_db
def test_index_view():
    user = User.objects.create(username="Moussa")
    Profile.objects.create(user=user, favorite_city="Paris")
    client = Client()
    response = client.get(reverse('profiles:index'))
    assert response.status_code == 200
    assert "Profiles" in response.content.decode()


@pytest.mark.django_db
def test_profile_view():
    user = User.objects.create(username="Moussa")
    Profile.objects.create(user=user, favorite_city="Paris")
    client = Client()
    response = client.get(reverse('profiles:profile', args=[user.username]))
    assert response.status_code == 200
    assert "Moussa" in response.content.decode()


def test_profiles_index_url():
    path = reverse('profiles:index')
    assert resolve(path).view_name == 'profiles:index'
    assert resolve(path).func == index


def test_profile_url():
    path = reverse('profiles:profile', args=['Moussa'])
    assert resolve(path).view_name == 'profiles:profile'
    assert resolve(path).func == profile
