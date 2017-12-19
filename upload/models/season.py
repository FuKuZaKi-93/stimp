from django.db import models


class Season(models.Model):
    season = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.season

