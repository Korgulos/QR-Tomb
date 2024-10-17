from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import SampleForm


def sample_post(request, *args, **kwargs):
    form = SampleForm(request.POST or None)

    if form.is_valid():
        print(f"{ form.cleaned_data = }")
        context = {"qr_text": form.cleaned_data["name"]}
        return render(request, "qr_template.html", context)

    else:
        return HttpResponse(
            '<p class="error">Please provide both name and email and favorite color.❌</p>'
        )


def example(request):

    text = "Trt Trt Trt"
    context = {"qr_text": text}

    return render(request, "example.html", context)
