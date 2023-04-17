from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'
