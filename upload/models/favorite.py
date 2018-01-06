from django.db import models
from django.contrib.auth.models import User

from upload.models.img import Img


class FavoriteImg(models.Model):
    user = models.ForeignKey(User, related_name='user')
    image = models.ForeignKey(Img, related_name='image')
