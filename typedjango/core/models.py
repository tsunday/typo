from django.db import models


class Driver(models.Model):
    position = models.PositiveIntegerField()  # type: models.PositiveIntegerField
    name = models.CharField(max_length=255)  # type: models.CharField

    objects = models.Manager()  # type: models.BaseManager
