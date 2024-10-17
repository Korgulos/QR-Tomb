# forms.py
from django import forms


class SampleForm(forms.Form):
    email = forms.CharField()
    name = forms.CharField(min_length=3)
    favorite_color = forms.CharField()
