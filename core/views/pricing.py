from django.shortcuts import render
from django.http import HttpResponse


def pricing(request):
    return render(request, "pricing.html")
