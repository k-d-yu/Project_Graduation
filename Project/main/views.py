from django.shortcuts import render, redirect
from .models import About, Session
from personal_account.models import Profile
from personal_account.forms import FeedbackForm
from django.contrib import messages
from main.models import Feedback
from django.contrib.auth.decorators import login_required
from .models import MakeAnAppointment
from .forms import MakeAnAppointmentForm
import re
from sendmessage_in_tg import send_telegram


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


@login_required(login_url="personal_account:login")
def reviews_delete(request):
    profile = request.user.profile
    feedbacks = profile.feedback_set.all()

    if request.method == "POST":
        feedbacks.delete()
        return redirect('reviews')

    context = {'profile': profile, 'feedbacks': feedbacks}
    return render(request, "main/reviews_delete.html", context)


def make_an_appointment(request):
    form = MakeAnAppointmentForm()
    context = {'form': form}
    return render(request, "main/make_an_appointment.html", context)


def thanks(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        pattern = "^\\+?[1-9][0-9]{7,14}$"
        reg = re.findall(pattern, phone)

        if reg:
            appointment = MakeAnAppointment(name=name, phone=phone)
            appointment.save()
            send_telegram(tg_name=name, tg_phone=phone)
            return render(request, "main/thanks.html", {'name': name})
        else:
            messages.error(request, "Некорректно указан номер телефона!")
            return redirect('make_an_appointment')

    else:
        return render(request, "main/thanks.html")