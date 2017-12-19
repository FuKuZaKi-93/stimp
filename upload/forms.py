from django import forms
from .models import (
    img, situation, color, member, season, place,
)
from django.contrib.auth.models import User

from PIL import Image



 

class  SituationForm(forms.ModelForm):
    class Meta:
        model = situation.Situation
        fields = ('situation',)
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


class PlaceForm(forms.ModelForm):
    class Meta:
        model = place.Place
        fields = ('place',)
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


class MemberForm(forms.ModelForm):
    class Meta:
        model = member.Member
        fields = ('member',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            field.widget.attrs["class"] = "form-control"



class ImgForm(forms.ModelForm):

    situation = forms.ModelMultipleChoiceField(
        label="催しの趣旨",
        queryset=situation.Situation.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    place = forms.ModelMultipleChoiceField(
        label="会場",
        queryset=place.Place.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    season = forms.ModelMultipleChoiceField(
        label="時期",
        queryset=season.Season.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    member = forms.ModelMultipleChoiceField(
        label="参加者",
        queryset=member.Member.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    color = forms.ModelMultipleChoiceField(
        label="服の色",
        queryset=color.Color.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = img.Img
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

"""
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
"""
