from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Имя пользователя')
    username = models.CharField(max_length=200, null=True, blank=True, verbose_name='Имя пользователя')
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Имя')
    surname = models.CharField(max_length=200, null=True, blank=True, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=200, null=True, blank=True, verbose_name='Отчество')
    email = models.EmailField(max_length=500, null=False, blank=False)
    phoneNumber = PhoneNumberField(null=True, blank=True, verbose_name='Номер телефона')
    secondPhoneNumber = PhoneNumberField(null=True, blank=True, verbose_name='Доп. номер телефона')
    bio = models.TextField(null=True, blank=True, verbose_name='О себе')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/user-default.png', verbose_name='Фото')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

