from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, ProfileForm
from .models import Appointment
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('personal_account:profile_user')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "Имени пользователя не существует")
            return redirect('personal_account:login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Вход выполнен")
            return redirect('personal_account:profile_user')
        else:
            messages.error(request, "Неверный логин или пароль")

    return render(request, "personal_account/login.html")


def logout_user(request):
    logout(request)
    messages.info(request, "Вы вышли из системы")
    return redirect('personal_account:login')


def register_user(request):
    page = 'register'
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "Аккаунт создан")
            login(request, user)
            return redirect('personal_account:profile_user')
        else:
            messages.error(request, "При регистрации ошибка")

    context = {"page": page, "form": form}
    return render(request, "personal_account/login.html", context)


@login_required(login_url="personal_account:login")
def profile_user(request):
    prof = request.user.profile
    context = {"profile": prof}
    return render(request, "personal_account/profile_user.html", context)


@login_required(login_url="personal_account:login")
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('personal_account:profile_user')

    context = {'form': form}
    return render(request, "personal_account/profile_form.html", context)


@login_required(login_url="personal_account:login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль успешно изменен!')
            return redirect('personal_account:profile_user')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'personal_account/change_password.html', {'form': form})


@login_required(login_url="personal_account:login")
def appointment(request):
    profile = request.user.profile
    form = profile.appointment_set.all()

    context = {'form': form}
    return render(request, 'personal_account/appointment.html', context)