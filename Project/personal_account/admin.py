from django.contrib import admin
from .models import Profile


class PersonalAccountAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)
    list_display = ('id', 'user', 'name', 'phoneNumber', 'created')
    list_display_links = ('id', 'user', 'name', 'phoneNumber', 'created')
    search_fields = ('name__iregex', 'phoneNumber')


admin.site.register(Profile, PersonalAccountAdmin)
