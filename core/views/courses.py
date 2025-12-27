from django.shortcuts import render
from django.http import HttpResponse


def courses(request):
    return render(request, "courses.html")
