from django.db import models
from django.contrib.auth.models import AbstractUser


class QrUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Qr(models.Model):
    user = models.ForeignKey(QrUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    qr_code = models.ImageField(upload_to="qr_codes/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class QrCode(models.Model):
    url_qr = (models.CharField(max_length=255, default=""),)
    dark_color_qr = (models.CharField(max_length=255, default="#000000"),)
    light_color_qr = (models.CharField(max_length=255, default="#ffffff"),)
    alignment_dark_color_qr = (models.CharField(max_length=255, default="#000000"),)
    alignment_light_color_qr = (models.CharField(max_length=255, default="#ffffff"),)
    dark_module_color_qr = (models.CharField(max_length=255, default="#000000"),)
    data_dark_color_qr = (models.CharField(max_length=255, default="#000000"),)
    data_light_color_qr = (models.CharField(max_length=255, default="#ffffff"),)
    finder_dark_color_qr = (models.CharField(max_length=255, default="#000000"),)
    finder_light_color_qr = (models.CharField(max_length=255, default="#ffffff"),)
    format_dark_color_qr = (models.CharField(max_length=255, default="#000000"),)
    format_light_color_qr = (models.CharField(max_length=255, default="#ffffff"),)
    quiet_zone_color_qr = (models.CharField(max_length=255, default="#ffffff"),)
    separator_color_qr = (models.CharField(max_length=255, default="#ffffff"),)
    timing_dark_color_qr = (models.CharField(max_length=255, default="#000000"),)
    timing_light_color_qr = (models.CharField(max_length=255, default="#ffffff"),)
    version_dark_color_qr = (models.CharField(max_length=255, default="#000000"),)
    version_light_color_qr = (models.CharField(max_length=255, default="#ffffff"),)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
