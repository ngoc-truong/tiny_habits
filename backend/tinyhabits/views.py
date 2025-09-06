from django.http import HttpResponse
from django.shortcuts import render

from .models import Aspiration


# Create your views here.
def index(request):
    latest_aspirations = Aspiration.objects.order_by("-pub_date")[:5]
    context = {"latest_aspirations": latest_aspirations}
    return render(request, "tinyhabits/index.html", context)
