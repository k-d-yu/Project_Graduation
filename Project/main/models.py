from django.db import models
from personal_account.models import Profile


class About(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'


class Session(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'


class Feedback(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner}'
