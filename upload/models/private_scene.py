from django.db import models


class PrivateScene(models.Model):
    private_scene = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.private_scene
