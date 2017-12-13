from django import forms
from .models import (
    Img, Situation, ClothColor, CoordinateStyle, Season, Purpose,
   # ITEM1_CHOICES, ITEM2_CHOICES,
    Comment,
)
from django.contrib.auth.models import User

from PIL import Image



 

class  SituationForm(forms.ModelForm):
    class Meta:
        model = Situation
        fields = ('situation',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            field.widget.attrs["class"] = "form-control"


class ColorForm(forms.ModelForm):
    class Meta:
        model = ClothColor
        fields = ('color',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            field.widget.attrs["class"] = "form-control"


class StyleForm(forms.ModelForm):
    class Meta:
        model = CoordinateStyle
        fields = ('style',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            field.widget.attrs["class"] = "form-control"


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ('season',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            field.widget.attrs["class"] = "form-control"


class PurposeForm(forms.ModelForm):
    class Meta:
        model = Purpose
        fields = ('purpose',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            field.widget.attrs["class"] = "form-control"



class ImgForm(forms.ModelForm):

    situation = forms.ModelMultipleChoiceField(
        queryset=Situation.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    color = forms.ModelMultipleChoiceField(
        queryset=ClothColor.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    style = forms.ModelMultipleChoiceField(
        queryset=CoordinateStyle.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    season = forms.ModelMultipleChoiceField(
        queryset=Season.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    purpose = forms.ModelMultipleChoiceField(
        queryset=Purpose.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
 
    class Meta:
        model = Img
        exclude = ('title', 'user',)

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


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
