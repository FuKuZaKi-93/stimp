from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from upload.models import img, situation, color, member, season, place, get_image_path

import os
import uuid
from PIL import Image



class Img(models.Model):
    title      = models.CharField("タイトル", max_length=255, blank=True)
    file       = models.ImageField("ファイル", upload_to=get_image_path)

    situation  = models.ManyToManyField(situation.Situation,)
    color      = models.ManyToManyField(color.Color,)
    member      = models.ManyToManyField(member.Member,)
    season     = models.ManyToManyField(season.Season,)
    place    = models.ManyToManyField(place.Place,)


    is_public  = models.BooleanField("未登録ユーザに公開", default=True)


    user       = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE,
                            blank=True, null=True)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)


    def __unicode__(self):
        return self.title

    def get_filename(self):
        return os.path.basename(self.file.name)
