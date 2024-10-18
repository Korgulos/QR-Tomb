from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import SampleForm


def create_qrcode_post(request, *args, **kwargs):
    form = SampleForm(request.POST or None)

    if form.is_valid():
        print(f"{ form = }")
        context = form.cleaned_data
        print(f"{ context['url_qr'] = }")
        return render(request, "positive_massage.html", context)

    else:
        return HttpResponse(
            '<p class="error">Please provide both name and email and favorite color.❌</p>'
        )


def example(request):

    text = "Trt Trt Trt"
    context = {"url_qr": text, "dark_color_qr": "#000000", "light_color_qr": "#ffffff"}
    print(f"{ context = }")
    return render(request, "example.html", context)
