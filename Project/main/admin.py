from django.contrib import admin
from .models import About, Session, Feedback


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class FeedbackAccountAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)
    list_display = ('id', 'owner', 'created')
    list_display_links = ('id', 'owner', 'created')


admin.site.register(Session, SessionAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Feedback, FeedbackAccountAdmin)