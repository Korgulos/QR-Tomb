# forms.py
from django import forms


class SampleForm(forms.Form):
    url_qr = forms.CharField()
    dark_color_qr = forms.CharField()
    light_color_qr = forms.CharField()
