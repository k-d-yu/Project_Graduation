from django.shortcuts import render
from .models import About, Session


def index(request):
    return render(request, "main/index.html")


def about(request):
    abouts = About.objects.all()
    context = {"abouts": abouts}
    return render(request, "main/about.html", context)


def session(request):
    sessions = Session.objects.all()
    context = {"sessions": sessions}
    return render(request, "main/session.html", context)


def contacts(request):
    return render(request, "main/contacts.html")