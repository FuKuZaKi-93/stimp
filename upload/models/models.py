from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 
 
import os
import uuid
from PIL import Image



CATEGORY_CHOICES = (
    ("後期中間発表で着る服", "後期中間発表で着る服"),
)

ITEM1_CHOICES = (
    ("item1-1", u"アイテム1-1"),
    ("item1-2", u"アイテム1-2"),
    ("item1-3", u"アイテム1-3"),
    ("item1-4", u"アイテム1-4"),
    ("item1-5", u"アイテム1-5"),
    ("item1-6", u"アイテム1-6"),
    ("item1-7", u"アイテム1-7"),
    ("item1-8", u"アイテム1-8"),
    ("item1-9", u"アイテム1-9"),
    ("item1-10", u"アイテム1-10"),
)

ITEM2_CHOICES = (
    ("item2-1", u"アイテム2-1"),
    ("item2-2", u"アイテム2-2"),
    ("item2-3", u"アイテム2-3"),
    ("item2-4", u"アイテム2-4"),
    ("item2-5", u"アイテム2-5"),
    ("item2-6", u"アイテム2-6"),
    ("item2-7", u"アイテム2-7"),
    ("item2-8", u"アイテム2-8"),
    ("item2-9", u"アイテム2-9"),
    ("item2-10", u"アイテム2-10"),
)


class Situation(models.Model):
    situation = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.situation


class ClothColor(models.Model):
    color = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.color


class CoordinateStyle(models.Model):
    style = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.style


class Season(models.Model):
    season = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.season


class Purpose(models.Model):
    purpose = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.purpose


def get_image_path(self, filename):
    prefix = 'images/'
    name = str(uuid.uuid4()).replace('-', '')
    extension = os.path.splitext(filename)[-1]
    return prefix + name + extension


class Img(models.Model):
    title      = models.CharField("タイトル", max_length=255, blank=True)
    file       = models.ImageField("ファイル", upload_to=get_image_path)

    situation  = models.ManyToManyField(Situation, verbose_name="状況")
    color      = models.ManyToManyField(ClothColor, verbose_name="色")
    style      = models.ManyToManyField(CoordinateStyle, verbose_name="スタイル")
    season     = models.ManyToManyField(Season, verbose_name="季節")
    purpose    = models.ManyToManyField(Purpose, verbose_name="意図")


    category   = models.CharField("お題", max_length=255,
                                choices=CATEGORY_CHOICES, blank=True)
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


class Comment(models.Model):
    text       = models.TextField("", blank=True)
    target     = models.ForeignKey(Img)
    created_at = models.DateTimeField(auto_now_add=True)
    user       = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    blank=True, null=True)

    def __str__(self):
        return self.text[:15]
