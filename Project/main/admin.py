from django.contrib import admin
from .models import About, Session, Feedback

admin.site.register(About)
admin.site.register(Session)


class FeedbackAccountAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)


admin.site.register(Feedback, FeedbackAccountAdmin)