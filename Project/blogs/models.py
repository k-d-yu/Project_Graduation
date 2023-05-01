from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/', default='default.jpg')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title