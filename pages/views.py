from django.shortcuts import render, get_object_or_404
from . import models


def page(request, slug):
    obj = get_object_or_404(models.Page, slug=slug)
    return render(request, "pages/page.html", {"page": obj})
