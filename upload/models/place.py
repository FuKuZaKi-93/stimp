from django.db import models


class Place(models.Model):
    place = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.place

