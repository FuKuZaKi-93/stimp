from django import forms
from .models import (
    img, buisiness_scene, private_scene, color, season, theme,
)
from django.contrib.auth.models import User

from PIL import Image



 

class  BuisinessSceneForm(forms.ModelForm):
    class Meta:
        model = buisiness_scene.BuisinessScene
        fields = ('buisiness_scene',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            field.widget.attrs["class"] = "form-control"


class PrivateSceneForm(forms.ModelForm):
    class Meta:
        model = private_scene.PrivateScene
        fields = ('private_scene',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            field.widget.attrs["class"] = "form-control"


class ColorForm(forms.ModelForm):
    class Meta:
        model = color.Color
        fields = ('color',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            field.widget.attrs["class"] = "form-control"


class ThemeForm(forms.ModelForm):
    class Meta:
        model = theme.Theme
        fields = ('theme',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            field.widget.attrs["class"] = "form-control"


class SeasonForm(forms.ModelForm):
    class Meta:
        model = season.Season
        fields = ('season',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            field.widget.attrs["class"] = "form-control"





class ImgForm(forms.ModelForm):
    
    buisiness_scene = forms.ModelMultipleChoiceField(
        label="ビジネス",
        queryset=buisiness_scene.BuisinessScene.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    private_scene = forms.ModelMultipleChoiceField(
        label="プライベート",
        queryset=private_scene.PrivateScene.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    season = forms.ModelMultipleChoiceField(
        label="季節",
        queryset=season.Season.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    color = forms.ModelMultipleChoiceField(
        label="メインカラー",
        queryset=color.Color.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    theme = forms.ModelMultipleChoiceField(
        label="テーマ",
        queryset=theme.Theme.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = img.Img
        exclude = ('user',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.value():
                field.widget.attrs["class"] = "form-control"
        widget = {
            'file' : forms.ClearableFileInput(attrs={
                'class': "form-control-file",
                'id'   : "upload-file",
            }),
        }

"""
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
"""
