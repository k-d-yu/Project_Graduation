from django.db import models
from personal_account.models import Profile


class About(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'


class Session(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Чем я смогу вам помочь'
        verbose_name_plural = 'Чем я смогу вам помочь'


class Feedback(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, verbose_name='Имя пользователя')
    body = models.TextField(null=True, blank=True, verbose_name='Отзыв')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return f'{self.owner}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
