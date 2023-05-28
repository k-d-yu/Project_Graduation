from django.contrib import admin
from .models import Profile, Appointment


class PersonalAccountAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)
    list_display = ('id', 'user', 'name', 'phoneNumber', 'created')
    list_display_links = ('id', 'user', 'name', 'phoneNumber', 'created')
    search_fields = ('name__iregex', 'phoneNumber')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'date')
    list_display_links = ('id', 'owner')


admin.site.register(Profile, PersonalAccountAdmin)
admin.site.register(Appointment, AppointmentAdmin)
