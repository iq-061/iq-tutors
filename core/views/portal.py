from django.shortcuts import render
from django.http import HttpResponse


def portal(request):
    return render(request, "portal.html")
