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
    alignment_dark_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "alignment_dark_color_qr",
                "placeholder": "Dark color for alignment Qr",
            }
        ),
        required=True,
    )
    alignment_light_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "alignment_light_color_qr",
                "placeholder": "Light color for alignment Qr",
                "value": "#ffffff",
            }
        ),
        required=True,
    )
    dark_module_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "dark_module_color_qr",
                "placeholder": "Dark color for module Qr",
            }
        ),
        required=True,
    )
    data_dark_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "data_dark_color_qr",
                "placeholder": "Dark color for data Qr",
            }
        ),
        required=True,
    )
    data_light_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "data_light_color_qr",
                "placeholder": "Light color for data Qr",
                "value": "#ffffff",
            }
        ),
        required=True,
    )
    finder_dark_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "finder_dark_color_qr",
                "placeholder": "Dark color for finder Qr",
            }
        ),
        required=True,
    )
    finder_light_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "finder_light_color_qr",
                "placeholder": "Light color for finder Qr",
                "value": "#ffffff",
            }
        ),
        required=True,
    )
    format_dark_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "format_dark_color_qr",
                "placeholder": "Dark color for format Qr",
            }
        ),
        required=True,
    )
    format_light_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "format_light_color_qr",
                "placeholder": "Light color for format Qr",
                "value": "#ffffff",
            }
        ),
        required=True,
    )
    quiet_zone_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "quiet_zone_color_qr",
                "placeholder": "Dark color for quiet zone Qr",
                "value": "#ffffff",
            }
        ),
        required=True,
    )
    separator_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "separator_color_qr",
                "placeholder": "Light color for separator Qr",
                "value": "#ffffff",
            }
        ),
        required=True,
    )
    timing_dark_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "timing_dark_color_qr",
                "placeholder": "Dark color for timing Qr",
            }
        ),
        required=True,
    )
    timing_light_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "timing_light_color_qr",
                "placeholder": "Light color for timing Qr",
                "value": "#ffffff",
            }
        ),
        required=True,
    )
    version_dark_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "version_dark_color_qr",
                "placeholder": "Dark color for version Qr",
            }
        ),
        required=True,
    )
    version_light_color_qr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "color",
                "name": "version_light_color_qr",
                "placeholder": "Light color for version Qr",
                "value": "#ffffff",
            }
        ),
        required=True,
    )
