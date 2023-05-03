from django.contrib import admin
from .models import Profile


class PersonalAccountAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)


admin.site.register(Profile, PersonalAccountAdmin)
