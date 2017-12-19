from django.contrib import admin
from .models import (
    img, situation, color, member, season, place,
)

admin.site.register((img.Img, situation.Situation, color.Color, member.Member, season.Season, place.Place,))
