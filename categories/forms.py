from django import forms
from .models import Theme
from datetimewidget.widgets import DateTimeWidget


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ('title',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.value():
                field.widget.attrs["class"] = "form-control"
"""
        dateTimeOptions = {
            'format': 'yyyy-mm-dd HH:ii:ss',
            'autoclose': True,
            'showMeridian': True
        }
        widgets = {
            'date': DateTimeWidget(options=dateTimeOptions)
        }
"""
