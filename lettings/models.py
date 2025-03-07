from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents an adress.

    Attributes:
        number (int): The street number.
        street (str): The name of the street.
        city (str): The name of the city.
        state (str): The state abreviation.
        zip_code (int): The ZIP code.
        country_iso_code (str): The ISO code of the country.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = 'Adresses'


class Letting(models.Model):
    """
    Represents a letting.

    Attributes:
        title (str): The title of the letting.
        address (Address): The address associated with the letting.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
