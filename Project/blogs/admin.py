from django.contrib import admin
from .models import Blogs


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ("date",)


admin.site.register(Blogs, BlogAdmin)