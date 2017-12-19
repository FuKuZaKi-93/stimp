from django.db import models


class Situation(models.Model):
    situation = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.situation

