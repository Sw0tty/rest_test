from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE)


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name