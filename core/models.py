from django.db import models
from datetime import date
# !Create your models here (all models here)


def default_json():
    return {'name': 'darko', 'position': 'Software Engineer'}


class Navbar(models.Model):
    # !props
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class About(models.Model):
    general_information = models.CharField(max_length=255)
    init_date = models.DateField(default=date.today)
    staff = models.JSONField(default=default_json)

    def __str__(self):
        return self.general_information


class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(max_length=255, default=100)

    def __str__(self):
        return self.name
