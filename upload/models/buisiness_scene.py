from django.db import models


class BuisinessScene(models.Model):
    buisiness_scene = models.CharField(max_length=255)

    def __str__(self):
        return self.buisiness_scene

