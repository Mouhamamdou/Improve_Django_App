import pytest
from .models import Address, Letting
from django.urls import reverse, resolve
from django.test import Client
from .views import index, letting


@pytest.mark.django_db
def test_address_model():
    address = Address.objects.create(
        number=7,
        street="Victor Hugo",
        city="Lille",
        state="HF",
        zip_code=59000,
        country_iso_code="FRA"
    )
    assert address.number == 7
    assert address.street == "Victor Hugo"


@pytest.mark.django_db
def test_letting_model():
    address = Address.objects.create(
        number=7,
        street="Victor Hugo",
        city="Lille",
        state="HF",
        zip_code=59000,
        country_iso_code="FRA"
    )
    letting = Letting.objects.create(title="Virage du Nord", address=address)
    assert letting.title == "Virage du Nord"
    assert letting.address == address


@pytest.mark.django_db
def test_index_view():
    address = Address.objects.create(
        number=7,
        street="Victor Hugo",
        city="Lille",
        state="HF",
        zip_code=59000,
        country_iso_code="FRA"
    )
    Letting.objects.create(title="Virage du Nord", address=address)
    client = Client()
    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200
    assert "Lettings" in response.content.decode()


@pytest.mark.django_db
def test_letting_view():
    address = Address.objects.create(
        number=7,
        street="Victor Hugo",
        city="Lille",
        state="HF",
        zip_code=59000,
        country_iso_code="FRA"
    )
    letting = Letting.objects.create(title="Virage du Nord", address=address)
    client = Client()
    response = client.get(reverse('lettings:letting', args=[letting.id]))
    assert response.status_code == 200
    assert "Virage du Nord" in response.content.decode()


def test_index_url():
    path = reverse('lettings:index')
    assert resolve(path).view_name == 'lettings:index'
    assert resolve(path).func == index


def test_letting_url():
    path = reverse('lettings:letting', args=[1])
    assert resolve(path).view_name == 'lettings:letting'
    assert resolve(path).func == letting
