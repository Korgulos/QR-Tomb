from django.urls import path

from . import views

urlpatterns = [
    path("", views.example, name="example"),
    path("create-qrcode-post/", views.create_qrcode_post, name="create-qrcode-post"),
]
