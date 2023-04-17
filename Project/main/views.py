from django.shortcuts import render
from .models import About


def index(request):
    return render(request, "main/index.html")


def about(request):
    abouts = About.objects.all()
    return render(request, "main/about.html", {"abouts": abouts})


def session(request):
    return render(request, "main/session.html")