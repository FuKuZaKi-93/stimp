from django.contrib import admin
from .models import (
    Img, Situation, ClothColor, CoordinateStyle, Season, Purpose,
)

admin.site.register((Img, Situation, ClothColor, CoordinateStyle, Season, Purpose,))
