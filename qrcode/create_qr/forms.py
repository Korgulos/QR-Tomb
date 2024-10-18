# forms.py
from django import forms


class QrForm(forms.Form):
    url_qr = forms.CharField(label="Url for Qr")
    dark_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "dark_color_qr",
                "placeholder": "Dark color for Qr",
            }
        ),
        required=True,
    )
    light_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "light_color_qr",
                "placeholder": "Light color for Qr",
                "value": "#ffffff",
            }
        ),
        required=True,
    )
