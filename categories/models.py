from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Theme (models.Model):
    title = models.CharField('お題', max_length=50, unique=True)
#    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.title
