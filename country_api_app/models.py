from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    population = models.BigIntegerField()
    area = models.FloatField(null=True, blank=True)
    language = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    major_cities = models.CharField(max_length=200)
    climate = models.CharField(max_length=200)
    currency = models.CharField(max_length=100)

    def __str__(self):
        return self.name