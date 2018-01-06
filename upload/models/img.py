from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from upload.models import img, buisiness_scene, private_scene, color, season, theme
from upload.models.get_image_path import get_image_path

import os
import uuid
from PIL import Image



class Img(models.Model):
    file       = models.ImageField("ファイル", upload_to=get_image_path)

    buisiness_scene  = models.ManyToManyField(buisiness_scene.BuisinessScene, blank=True)
    private_scene  = models.ManyToManyField(private_scene.PrivateScene, blank=True)
    season     = models.ManyToManyField(season.Season, blank=True)
    color      = models.ManyToManyField(color.Color, blank=True)
    theme      = models.ManyToManyField(theme.Theme, blank=True)

    message    = models.CharField("ひとことコメント", max_length=255, blank=True)

    is_public  = models.BooleanField("未登録ユーザに公開", default=True)


    user       = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE,
                            blank=True, null=True)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)


#    def __unicode__(self):
#        return self.title

    def get_filename(self):
        return os.path.basename(self.file.name)
