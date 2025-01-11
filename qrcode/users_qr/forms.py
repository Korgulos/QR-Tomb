from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import QrUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = QrUser
        fields = ["username", "email", "name", "surname", "bio", "profile_picture"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = QrUser
        fields = ["username", "email", "name", "surname", "bio", "profile_picture"]
