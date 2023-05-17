from django.contrib import admin
from .models import Blogs


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ("date",)
    list_display = ('id', 'title', 'date')
    list_display_links = ('id', 'title', 'date')
    search_fields = ('title__iregex', )


admin.site.register(Blogs, BlogAdmin)