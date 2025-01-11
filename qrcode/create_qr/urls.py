from django.urls import path

from . import views

urlpatterns = [
    path("", views.QrView.as_view(), name="index"),
    path("form_for_qr", views.form_for_qr, name="form_for_qr"),
    path("create-qrcode-post/", views.create_qrcode_post, name="create-qrcode-post"),
]
