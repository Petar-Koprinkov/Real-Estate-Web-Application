from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'real_estate_web_application.accounts'


    def ready(self):
        import real_estate_web_application.accounts.signals
