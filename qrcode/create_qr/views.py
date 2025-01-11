from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from .forms import QrForm


class QrView(View):
    html = ["qrcode/index.html"]

    def get(self, request):

        context = {
            "url_qr": "",
            "dark_color_qr": "#000000",
            "light_color_qr": "#ffffff",
            "alignment_dark_color_qr": "#000000",
            "alignment_light_color_qr": "#ffffff",
            "dark_module_color_qr": "#000000",
            "data_dark_color_qr": "#000000",
            "data_light_color_qr": "#ffffff",
            "finder_dark_color_qr": "#000000",
            "finder_light_color_qr": "#ffffff",
            "format_dark_color_qr": "#000000",
            "format_light_color_qr": "#ffffff",
            "quiet_zone_color_qr": "#ffffff",
            "separator_color_qr": "#ffffff",
            "timing_dark_color_qr": "#000000",
            "timing_light_color_qr": "#ffffff",
            "version_dark_color_qr": "#000000",
            "version_light_color_qr": "#ffffff",
            "form": QrForm(),
        }
        return render(request, "index.html", context)


def create_qrcode_post(request, *args, **kwargs):
    form = QrForm(request.POST or None)

    if form.is_valid():
        # print(f"{ form = }")
        context = _sort_color_qr_form(form.cleaned_data)
        print(f"{ context['data_light_color_qr'] = }")
        return render(request, "positive_massage.html", context)

    else:
        return HttpResponse(
            '<p class="error">Something went wrong QRcode not created.❌ </p>'
        )


def form_for_qr(request):

    context = {
        "url_qr": "",
        "dark_color_qr": "#000000",
        "light_color_qr": "#ffffff",
        "alignment_dark_color_qr": "#000000",
        "alignment_light_color_qr": "#ffffff",
        "dark_module_color_qr": "#000000",
        "data_dark_color_qr": "#000000",
        "data_light_color_qr": "#ffffff",
        "finder_dark_color_qr": "#000000",
        "finder_light_color_qr": "#ffffff",
        "format_dark_color_qr": "#000000",
        "format_light_color_qr": "#ffffff",
        "quiet_zone_color_qr": "#ffffff",
        "separator_color_qr": "#ffffff",
        "timing_dark_color_qr": "#000000",
        "timing_light_color_qr": "#ffffff",
        "version_dark_color_qr": "#000000",
        "version_light_color_qr": "#ffffff",
        "form": QrForm(),
    }
    print(f"{ context = }")
    return render(request, "qr_form.html", context)


def _sort_color_qr_form(form):
    if form["dark_color_qr"] != "#000000":
        if form["alignment_dark_color_qr"] == "#000000":
            form["alignment_dark_color_qr"] = form["dark_color_qr"]
        if form["dark_module_color_qr"] == "#000000":
            form["dark_module_color_qr"] = form["dark_color_qr"]
        if form["data_dark_color_qr"] == "#000000":
            form["data_dark_color_qr"] = form["dark_color_qr"]
        if form["finder_dark_color_qr"] == "#000000":
            form["finder_dark_color_qr"] = form["dark_color_qr"]
        if form["format_dark_color_qr"] == "#000000":
            form["format_dark_color_qr"] = form["dark_color_qr"]
        if form["timing_dark_color_qr"] == "#000000":
            form["timing_dark_color_qr"] = form["dark_color_qr"]
        if form["version_dark_color_qr"] == "#000000":
            form["version_dark_color_qr"] = form["dark_color_qr"]

    if form["light_color_qr"] != "#ffffff":
        if form["alignment_light_color_qr"] == "#ffffff":
            form["alignment_light_color_qr"] = form["light_color_qr"]
        if form["data_light_color_qr"] == "#ffffff":
            form["data_light_color_qr"] = form["light_color_qr"]
        if form["finder_light_color_qr"] == "#ffffff":
            form["finder_light_color_qr"] = form["light_color_qr"]
        if form["format_light_color_qr"] == "#ffffff":
            form["format_light_color_qr"] = form["light_color_qr"]
        if form["quiet_zone_color_qr"] == "#ffffff":
            form["quiet_zone_color_qr"] = form["light_color_qr"]
        if form["separator_color_qr"] == "#ffffff":
            form["separator_color_qr"] = form["light_color_qr"]
        if form["timing_light_color_qr"] == "#ffffff":
            form["timing_light_color_qr"] = form["light_color_qr"]
        if form["version_light_color_qr"] == "#ffffff":
            form["version_light_color_qr"] = form["light_color_qr"]

    return form
