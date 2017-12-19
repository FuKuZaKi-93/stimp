from django.db import models


class Member(models.Model):
    member = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.member
