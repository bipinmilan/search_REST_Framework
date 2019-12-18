from django.db import models
from smart_selects.db_fields import GroupedForeignKey


# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=30)

    def __str__(self):
        return self.country_name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return self.city_name


class Person(models.Model):
    person_name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    # city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    city = GroupedForeignKey(City, "country", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.person_name
