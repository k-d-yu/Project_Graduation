from django.apps import AppConfig


class PersonalAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personal_account'

    def ready(self):
        import personal_account.signals
