from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from inventory.models import *

def index(request):
    # added
    artists = Artist.objects.all()

    # changed
    return render(request, "inventory/index.html", locals())