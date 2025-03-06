from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'payment'

    def ready(self):
        # Do not access models or the database here directly
        pass
