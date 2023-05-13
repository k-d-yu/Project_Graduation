from django.shortcuts import render, redirect
from .models import About, Session
from personal_account.models import Profile
from personal_account.forms import FeedbackForm
from django.contrib import messages
from main.models import Feedback


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


def reviews(request):
    profiles = Profile.objects.all()
    form = FeedbackForm()

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        feedback = form.save(commit=False)
        feedback.owner = request.user.profile
        feedback.save()
        messages.success(request, "Ваш отзыв успешно отправлен")
        return redirect('reviews')

    try:
        profile = Profile.objects.filter(user=request.user)
        feedbacks = Feedback.objects.all().values_list('owner__id', flat=True)
    except:
        profile = None
        feedbacks = None

    context = {"profiles": profiles, "form": form, "profile": profile, "feedbacks": feedbacks}
    return render(request, "main/reviews.html", context)