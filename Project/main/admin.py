from django.contrib import admin
from .models import About, Session, Feedback, MakeAnAppointment


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


class MakeAnAppointmentAdmin(admin.ModelAdmin):
    readonly_fields = ("date",)
    list_display = ('id', 'name', 'phone', 'date')
    list_display_links = ('id', 'name', 'phone', 'date')
    search_fields = ('id', 'name', 'phone', 'date')


admin.site.register(Session, SessionAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Feedback, FeedbackAccountAdmin)
admin.site.register(MakeAnAppointment, MakeAnAppointmentAdmin)