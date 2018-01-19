from django.contrib import admin
from .models import (
    img,
    buisiness_scene,
    private_scene,
    color,
    season,
    theme,
    like,
    rate,
)

admin.site.register((img.Img,
                    buisiness_scene.BuisinessScene,
                    private_scene.PrivateScene,
                    color.Color,
                    season.Season,
                    theme.Theme,

                    like.Like,
                    rate.Rate))
