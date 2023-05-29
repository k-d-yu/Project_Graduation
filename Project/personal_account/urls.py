from django.urls import path
from . import views
from .views import *


app_name = "personal_account"

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('profile_user/', views.profile_user, name="profile_user"),
    path('register/', views.register_user, name="register"),
    path('edit_account/', views.edit_account, name="edit_account"),
    path('password/', views.change_password, name="change_password"),
    path('appointment/', views.appointment, name="appointment"),

    path('password-reset/', UserForgotPasswordView.as_view(), name='password-reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password-reset-confirm')
]