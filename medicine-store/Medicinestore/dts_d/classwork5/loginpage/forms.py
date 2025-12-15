from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def validate_not_gmail(value):
    if value.find('@gmail') != -1:
        raise ValidationError(
            "Gmail is not allowed",
            params={'value': value},
        )
class LoginForm(forms.Form):
    email = forms.CharField(label='email',validators=[validate_email,validate_not_gmail],max_length=100)
    password = forms.CharField(label='password',min_length=6,widget=forms.PasswordInput)