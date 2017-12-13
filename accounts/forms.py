from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

password = forms.RegexField(
    max_length=16,
    min_length=8,
    regex=r'^[a-zA-Z][a-zA-Z0-9]+$',
    error_messages={
        'invalid': _('先頭を半角英字から始めて、8〜16文字の半角英数字で入力してください。'),
    },
    widget=forms.PasswordInput,
)

class CustomUserCreationForm(UserCreationForm):
    username = forms.RegexField(
        max_length=16,
        min_length=3,
        regex=r'^[a-z][a-zA-Z0-9]+$',
        error_messages={
            'invalid': _('先頭を小文字の半角英字から始めて、3〜8文字の半角英数字で入力してください。'),
        },
    )
    password1 = password
    password2 = password

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = (
            'username',
        )



class SigninForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password'].widget.attrs['placeholder'] = 'password'

