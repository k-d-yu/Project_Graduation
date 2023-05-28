from django.urls import path
from . import views


app_name = "personal_account"

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('profile_user/', views.profile_user, name="profile_user"),
    path('register/', views.register_user, name="register"),
    path('edit_account/', views.edit_account, name="edit_account"),
    path('password/', views.change_password, name="change_password"),
]